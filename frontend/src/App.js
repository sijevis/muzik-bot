import React, { useState, useEffect, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { useTheme } from './context/ThemeContext';
import { useAuth } from './context/AuthContext';
import Sidebar from './components/Sidebar';
import ChatArea from './components/ChatArea';
import PlaylistView from './components/PlaylistView';
import AuthPage from './components/AuthPage';
import SharePlaylistModal from './components/SharePlaylistModal';
import SpotifyConnectModal from './components/SpotifyConnectModal';
import {
  sendMessage,
  getCategories,
  getStatus,
  getUserPreferences,
  getUserPlaylists,
  resetSession,
  renamePlaylist,
  getSpotifyStatus,
} from './services/api';

const WELCOME_MESSAGE = {
  id: 'welcome',
  role: 'assistant',
  content:
    'Merhaba! Ben DJ AI, senin kişisel müzik danışmanın! 🎵\n\n' +
    'Sana nasıl yardımcı olabilirim? Ne tür müzik istersin?\n\n' +
    '🎸 Hangi müzik türünü istersen söyle\n' +
    '😊 Şu an nasıl hissediyorsan anlat\n' +
    '🏃 Hangi aktivite için müzik arıyorsan belirt\n' +
    '📋 "Bana playlist yap" yazarak başla\n\n' +
    'Aşağıdaki kategorilere de tıklayabilirsin! 🎶',
  timestamp: new Date(),
  songs: [],
  ask_more: false,
};

const App = () => {
  const { isDark } = useTheme();
  const { getUserId, isAuthenticated, user } = useAuth();
  const [sessionId] = useState(() => uuidv4());
  const [userId] = useState(() => {
    const stored = localStorage.getItem('muzikbot-user-id');
    if (stored) return stored;
    const newId = uuidv4();
    localStorage.setItem('muzikbot-user-id', newId);
    return newId;
  });

  const [messages, setMessages] = useState([WELCOME_MESSAGE]);
  const [isTyping, setIsTyping] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(window.innerWidth >= 1024);
  const [isDemoMode, setIsDemoMode] = useState(true);
  const [currentPlaylist, setCurrentPlaylist] = useState(null);
  const [categories, setCategories] = useState([]);
  const [preferences, setPreferences] = useState(null);
  const [savedPlaylists, setSavedPlaylists] = useState([]);
  const [showShareModal, setShowShareModal] = useState(false);
  const [viewingPlaylist, setViewingPlaylist] = useState(null);
  const [isAuthed, setIsAuthed] = useState(false);
  const [showSpotifyConnect, setShowSpotifyConnect] = useState(false);
  const [spotifyConnected, setSpotifyConnected] = useState(false);

  useEffect(() => {
    if (!isAuthed) return;
    const initData = async () => {
        try {
          const uid = user?.uid || getUserId();
          const [cats, status, prefs, playlists] = await Promise.all([
            getCategories(),
            getStatus(),
            getUserPreferences(uid).catch(() => null),
            getUserPlaylists(uid).catch(() => []),
          ]);
          setCategories(cats);
          setIsDemoMode(status.demo_mode || false);
          if (prefs) setPreferences(prefs);
          if (playlists) setSavedPlaylists(playlists);
        } catch {
          setCategories([
            { label: "Playlist Yap", message: "Bana karışık playlist yap", icon: "📋" },
            { label: "Rock", message: "Bana rock müzik öner", icon: "🎸" },
            { label: "Motivasyon", message: "Motivasyona ihtiyacım var", icon: "💪" },
            { label: "Sakinleş", message: "Sakinleşmek istiyorum", icon: "🧘" },
          ]);
        }
        try {
          const uid = user?.uid || userId;
          const status = await getSpotifyStatus(uid);
          setSpotifyConnected(status.spotify_connected || false);
        } catch {
          setSpotifyConnected(false);
        }
      };
    initData();
  }, [isAuthed, userId, user, getUserId]);

  const refreshUserData = useCallback(async () => {
    try {
      const uid = user?.uid || getUserId();
      const [prefs, playlists] = await Promise.all([
        getUserPreferences(uid).catch(() => null),
        getUserPlaylists(uid).catch(() => []),
      ]);
      if (prefs) setPreferences(prefs);
      if (playlists) setSavedPlaylists(playlists);
    } catch {}
  }, [user, getUserId]);

  const sendChatMessage = useCallback(
    async (userMessage) => {
      if (!userMessage.trim() || isTyping) return;

      const userMsg = {
        id: Date.now(),
        role: 'user',
        content: userMessage,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, userMsg]);
      setCurrentPlaylist(null);
      setIsTyping(true);

      try {
        const uid = user?.uid || getUserId();
        const data = await sendMessage(userMessage, sessionId, uid);

        const botMsg = {
          id: Date.now() + 1,
          role: 'assistant',
          content: data.message || '',
          songs: data.songs || [],
          timestamp: new Date(),
          playlistQuestion: data.playlist_question || null,
        };
        setMessages((prev) => [...prev, botMsg]);

        if (data.playlist) {
          setCurrentPlaylist(data.playlist);
          refreshUserData();
        }

        if (data.demo_mode !== undefined) {
          setIsDemoMode(data.demo_mode);
        }
      } catch (error) {
        const errorMsg = {
          id: Date.now() + 1,
          role: 'assistant',
          content: error.message || 'Bağlantı hatası oluştu. Lütfen tekrar deneyin.',
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, errorMsg]);
      } finally {
        setIsTyping(false);
      }
    },
    [sessionId, isTyping, user, getUserId, refreshUserData]
  );

  const handleReset = useCallback(async () => {
    await resetSession(sessionId, getUserId());
    setMessages([WELCOME_MESSAGE]);
    setCurrentPlaylist(null);
  }, [sessionId, getUserId]);

  const handleCategoryClick = useCallback(
    (message) => {
      sendChatMessage(message);
    },
    [sendChatMessage]
  );

  const handleSavePlaylist = useCallback(async (name) => {
    if (currentPlaylist?.id && name) {
      await renamePlaylist(currentPlaylist.id, name);
      refreshUserData();
    }
  }, [currentPlaylist, refreshUserData]);

  const handleViewPlaylist = useCallback((playlist) => {
    setViewingPlaylist(playlist);
  }, []);

  const handleLogin = useCallback((userData) => {
    setIsAuthed(true);
    refreshUserData();
  }, [refreshUserData]);

  const handleGuest = useCallback(() => {
    setIsAuthed(true);
  }, []);

  const handleLogout = useCallback(() => {
    setIsAuthed(false);
    setMessages([WELCOME_MESSAGE]);
    setCurrentPlaylist(null);
    setCategories([]);
    setPreferences(null);
    setSavedPlaylists([]);
    setSpotifyConnected(false);
  }, []);

  const handleSpotifyConnected = useCallback((connected) => {
    setSpotifyConnected(connected);
  }, []);

  if (!isAuthed) {
    return <AuthPage onLogin={handleLogin} onGuest={handleGuest} />;
  }

  return (
    <div className={`flex h-screen overflow-hidden ${isDark ? 'bg-dark-950 text-white' : 'bg-gray-50 text-gray-900'}`}>
      <Sidebar
        categories={categories}
        onCategoryClick={handleCategoryClick}
        onReset={handleReset}
        isDemoMode={isDemoMode}
        playlists={savedPlaylists}
        onCloseSidebar={() => setSidebarOpen(false)}
        isOpen={sidebarOpen}
        preferences={preferences}
        onViewPlaylist={handleViewPlaylist}
        onArtistClick={(artistName) => sendChatMessage(`${artistName} dinlemek istiyorum`)}
        onPlaylistDeleted={refreshUserData}
        onLogout={handleLogout}
        onOpenSpotifyConnect={() => setShowSpotifyConnect(true)}
        spotifyConnected={spotifyConnected}
      />

      <div className="flex-1 flex flex-col h-full overflow-hidden lg:ml-0">
        <ChatArea
          messages={messages}
          onSendMessage={sendChatMessage}
          isTyping={isTyping}
          onToggleSidebar={() => setSidebarOpen((prev) => !prev)}
          preferences={preferences}
        />

        {(currentPlaylist && currentPlaylist.songs && currentPlaylist.songs.length > 0) && (
          <PlaylistView
            playlist={currentPlaylist}
            isDark={isDark}
            onClose={() => setCurrentPlaylist(null)}
            onShare={() => setShowShareModal(true)}
          />
        )}

        {(viewingPlaylist && viewingPlaylist.songs && viewingPlaylist.songs.length > 0) && (
          <PlaylistView
            playlist={viewingPlaylist}
            isDark={isDark}
            onClose={() => setViewingPlaylist(null)}
          />
        )}
      </div>

      {!sidebarOpen && (
        <button
          onClick={() => setSidebarOpen(true)}
          className={`fixed top-4 left-4 z-30 p-2 rounded-lg shadow-lg transition-all lg:hidden ${
            isDark
              ? 'bg-dark-800 hover:bg-dark-700 text-gray-300 border border-dark-600'
              : 'bg-white hover:bg-gray-50 text-gray-600 border border-gray-200'
          }`}
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      )}

      <SharePlaylistModal
        isOpen={showShareModal}
        onClose={() => setShowShareModal(false)}
        playlist={currentPlaylist}
        isDark={isDark}
        onSave={handleSavePlaylist}
        userId={user?.uid || getUserId()}
        spotifyConnected={spotifyConnected}
        onOpenSpotifyConnect={() => { setShowShareModal(false); setShowSpotifyConnect(true); }}
      />

      <SpotifyConnectModal
        isOpen={showSpotifyConnect}
        onClose={() => setShowSpotifyConnect(false)}
        onConnected={handleSpotifyConnected}
      />
    </div>
  );
};

export default App;