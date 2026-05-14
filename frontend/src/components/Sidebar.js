import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTheme } from '../context/ThemeContext';
import { useAuth } from '../context/AuthContext';
import { getArtists, deletePlaylist, getSpotifyStatus } from '../services/api';

const Sidebar = ({
  categories,
  onCategoryClick,
  onReset,
  isDemoMode,
  playlists,
  onCloseSidebar,
  isOpen,
  preferences,
  onViewPlaylist,
  onArtistClick,
  onPlaylistDeleted,
  onLogout,
  onOpenSpotifyConnect,
  spotifyConnected,
}) => {
  const { isDark, toggleTheme } = useTheme();
  const { user, isAuthenticated, logout } = useAuth();
  const [activeTab, setActiveTab] = useState('categories');
  const [artists, setArtists] = useState([]);
  const [artistSearch, setArtistSearch] = useState('');

  useEffect(() => {
    if (activeTab === 'artists' && artists.length === 0) {
      getArtists().then(setArtists).catch(() => {});
    }
  }, [activeTab, artists.length]);

  const filteredArtists = artistSearch
    ? artists.filter(a => a.name.toLowerCase().includes(artistSearch.toLowerCase()))
    : artists;

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black/50 z-40 lg:hidden"
            onClick={onCloseSidebar}
          />
          <motion.aside
            initial={{ x: -288 }}
            animate={{ x: 0 }}
            exit={{ x: -288 }}
            transition={{ type: 'spring', damping: 25, stiffness: 200 }}
            className={`fixed lg:relative z-50 h-full w-72 flex flex-col border-r ${
              isDark ? 'bg-dark-900 border-dark-700' : 'bg-white border-gray-200'
            }`}
          >
            <div className={`p-4 border-b ${isDark ? 'border-dark-700' : 'border-gray-200'}`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full gradient-primary flex items-center justify-center text-white text-xl">
                    🎵
                  </div>
                  <div>
                    <h1 className={`font-bold text-lg ${isDark ? 'text-white' : 'text-gray-900'}`}>
                      DJ AI
                    </h1>
                    <p className={`text-xs ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                      AI Müzik Asistanın
                    </p>
                  </div>
                </div>
                <button
                  onClick={onCloseSidebar}
                  className={`lg:hidden p-2 rounded-lg ${
                    isDark ? 'hover:bg-dark-700 text-gray-400' : 'hover:bg-gray-100 text-gray-500'
                  }`}
                >
                  ✕
                </button>
              </div>

{isDemoMode && (
                 <div className={`mt-3 px-3 py-1.5 rounded-lg text-xs font-medium ${
                   isDark ? 'bg-yellow-500/10 text-yellow-400 border border-yellow-500/20' : 'bg-yellow-50 text-yellow-600 border border-yellow-200'
                 }`}>
                   ⚡ Demo Modu
                 </div>
               )}

               <button
                 onClick={onOpenSpotifyConnect}
                 className={`mt-3 w-full flex items-center gap-2 px-3 py-2 rounded-lg text-xs font-medium transition-all ${
                   spotifyConnected
                     ? isDark ? 'bg-[#1DB954]/10 text-[#1DB954] border border-[#1DB954]/20 hover:bg-[#1DB954]/20' : 'bg-green-50 text-green-600 border border-green-200 hover:bg-green-100'
                     : isDark ? 'bg-dark-800 text-gray-300 border border-dark-600 hover:bg-dark-700' : 'bg-gray-50 text-gray-600 border border-gray-200 hover:bg-gray-100'
                 }`}
               >
                 <svg className="w-4 h-4 flex-shrink-0" viewBox="0 0 24 24" fill="currentColor">
                   <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.54.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.301z"/>
                 </svg>
                 <span className="flex-1 text-left">
                   {spotifyConnected ? 'Spotify Bağlı' : 'Spotify Bağla'}
                 </span>
                 {spotifyConnected && (
                   <span className="w-2 h-2 rounded-full bg-[#1DB954] flex-shrink-0" />
                 )}
               </button>
             </div>

            <div className={`p-3 border-b ${isDark ? 'border-dark-700' : 'border-gray-200'}`}>
              {isAuthenticated ? (
                <div className="flex items-center gap-2">
                  {user?.photoURL ? (
                    <img src={user.photoURL} alt={user.displayName} className="w-8 h-8 rounded-full" />
                  ) : (
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm ${
                      isDark ? 'bg-primary-500/20 text-primary-300' : 'bg-primary-100 text-primary-600'
                    }`}>
                      {user?.displayName?.[0] || '👤'}
                    </div>
                  )}
                  <div className="flex-1 min-w-0">
                    <p className={`text-sm font-medium truncate ${isDark ? 'text-white' : 'text-gray-800'}`}>
                      {user?.displayName || 'Kullanıcı'}
                    </p>
                    <p className={`text-[10px] truncate ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                      {user?.email || ''}
                    </p>
                  </div>
                </div>
) : (
                 <div className={`text-sm ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                   👤 Misafir
                 </div>
               )}
             </div>

            <div className={`flex border-b ${isDark ? 'border-dark-700' : 'border-gray-200'}`}>
              <button
                onClick={() => setActiveTab('categories')}
                className={`flex-1 py-2.5 text-[10px] font-medium transition-colors ${
                  activeTab === 'categories'
                    ? isDark ? 'text-primary-400 border-b-2 border-primary-400' : 'text-primary-600 border-b-2 border-primary-600'
                    : isDark ? 'text-gray-400 hover:text-gray-200' : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Kategoriler
              </button>
              <button
                onClick={() => setActiveTab('playlists')}
                className={`flex-1 py-2.5 text-[10px] font-medium transition-colors ${
                  activeTab === 'playlists'
                    ? isDark ? 'text-primary-400 border-b-2 border-primary-400' : 'text-primary-600 border-b-2 border-primary-600'
                    : isDark ? 'text-gray-400 hover:text-gray-200' : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Playlistlerim
              </button>
              <button
                onClick={() => setActiveTab('artists')}
                className={`flex-1 py-2.5 text-[10px] font-medium transition-colors ${
                  activeTab === 'artists'
                    ? isDark ? 'text-primary-400 border-b-2 border-primary-400' : 'text-primary-600 border-b-2 border-primary-600'
                    : isDark ? 'text-gray-400 hover:text-gray-200' : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Sanatçılar
              </button>
            </div>

            <div className="flex-1 overflow-y-auto p-3">
              <AnimatePresence mode="wait">
                {activeTab === 'categories' ? (
                  <motion.div
                    key="categories"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    className="flex flex-col gap-1"
                  >
                    {categories.reduce((acc, cat, idx) => {
                      if (cat.section) {
                        acc.push(
                          <div key={`section-${idx}`} className={`mt-3 mb-1 px-1 text-[10px] font-semibold uppercase tracking-wider ${isDark ? 'text-gray-500' : 'text-gray-400'}`}>
                            {cat.label}
                          </div>
                        );
                      } else {
                        acc.push(
                          <motion.button
                            key={idx}
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ delay: idx * 0.02 }}
                            onClick={() => {
                              onCategoryClick(cat.message);
                              if (window.innerWidth < 1024) onCloseSidebar();
                            }}
                            className={`category-chip text-left ${
                              isDark ? 'category-chip-dark' : 'category-chip-light'
                            }`}
                          >
                            <span className="mr-2">{cat.icon}</span>
                            {cat.label}
                          </motion.button>
                        );
                      }
                      return acc;
                    }, [])}

                    {preferences && (preferences.liked_genres?.length > 0) && (
                      <div className={`mt-4 p-3 rounded-xl ${isDark ? 'bg-dark-800 border border-dark-600' : 'bg-gray-50 border border-gray-200'}`}>
                        <h3 className={`text-xs font-semibold mb-2 ${isDark ? 'text-gray-300' : 'text-gray-600'}`}>
                          Sevdiğin Türler
                        </h3>
                        <div className="flex flex-wrap gap-1.5">
                          {preferences.liked_genres.slice(0, 6).map((genre, i) => (
                            <span key={i} className={`px-2 py-0.5 rounded-full text-[10px] ${
                              isDark ? 'bg-primary-500/20 text-primary-300' : 'bg-primary-100 text-primary-700'
                            }`}>
                              {genre}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </motion.div>
                ) : activeTab === 'playlists' ? (
                  <motion.div
                    key="playlists"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    className="flex flex-col gap-2"
                  >
                    {playlists && playlists.length > 0 ? (
                      playlists.map((pl, idx) => (
                        <div
                          key={idx}
                          className={`p-3 rounded-xl cursor-pointer transition-colors ${
                            isDark ? 'bg-dark-800 hover:bg-dark-700 border border-dark-600' : 'bg-gray-50 hover:bg-gray-100 border border-gray-200'
                          }`}
                        >
                          <div className="flex items-center justify-between">
                            <span
                              className={`text-sm font-medium ${isDark ? 'text-white' : 'text-gray-800'} cursor-pointer flex-1`}
                              onClick={() => {
                                if (pl.songs && pl.songs.length > 0) {
                                  onViewPlaylist && onViewPlaylist(pl);
                                  if (window.innerWidth < 1024) onCloseSidebar();
                                }
                              }}
                            >
                              🎵 {pl.name}
                            </span>
                            <div className="flex items-center gap-2">
                              <span className={`text-xs ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                                {pl.song_count} şarkı
                              </span>
                              <button
                                onClick={async (e) => {
                                  e.stopPropagation();
                                  if (window.confirm(`"${pl.name}" playlistini silmek istediğinize emin misiniz?`)) {
                                    await deletePlaylist(pl.id, '');
                                    onPlaylistDeleted && onPlaylistDeleted();
                                  }
                                }}
                                className={`p-1 rounded transition-colors ${
                                  isDark ? 'text-gray-500 hover:text-red-400 hover:bg-dark-600' : 'text-gray-400 hover:text-red-500 hover:bg-gray-200'
                                }`}
                                title="Playlist'i sil"
                              >
                                <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                </svg>
                              </button>
                            </div>
                          </div>
                          {pl.description && (
                            <p className={`text-xs mt-1 line-clamp-2 ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                              {pl.description}
                            </p>
                          )}
                        </div>
                      ))
                    ) : (
                      <div className={`text-center py-8 ${isDark ? 'text-gray-500' : 'text-gray-400'}`}>
                        <p className="text-3xl mb-2">🎶</p>
                        <p className="text-xs">Henüz playlist yok</p>
                        <p className="text-xs mt-1">"Playlist yap" yazarak başla!</p>
                      </div>
                    )}
                  </motion.div>
                ) : (
                  <motion.div
                    key="artists"
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -10 }}
                    className="flex flex-col gap-2"
                  >
                    <input
                      type="text"
                      value={artistSearch}
                      onChange={(e) => setArtistSearch(e.target.value)}
                      placeholder="Sanatçı ara..."
                      className={`w-full px-3 py-2 rounded-lg text-xs outline-none ${
                        isDark ? 'bg-dark-800 border border-dark-600 text-white placeholder-gray-500 focus:border-primary-500' : 'bg-gray-50 border border-gray-200 text-gray-900 placeholder-gray-400 focus:border-primary-500'
                      }`}
                    />
                    <div className="max-h-[60vh] overflow-y-auto space-y-1">
                      {filteredArtists.map((artist, idx) => (
                        <button
                          key={idx}
                          onClick={() => {
                            onArtistClick && onArtistClick(artist.name);
                            if (window.innerWidth < 1024) onCloseSidebar();
                          }}
                          className={`w-full text-left p-2 rounded-lg transition-colors flex items-center justify-between group ${
                            isDark ? 'hover:bg-dark-700' : 'hover:bg-gray-100'
                          }`}
                        >
                          <div className="min-w-0">
                            <p className={`text-xs font-medium truncate ${isDark ? 'text-white' : 'text-gray-800'}`}>
                              {artist.name}
                            </p>
                            <p className={`text-[10px] truncate ${isDark ? 'text-gray-500' : 'text-gray-400'}`}>
                              {artist.genres.slice(0, 3).join(', ')} • {artist.song_count} şarkı
                            </p>
                          </div>
                          <span className={`text-[10px] opacity-0 group-hover:opacity-100 transition-opacity ${
                            isDark ? 'text-primary-400' : 'text-primary-600'
                          }`}>
                            →
                          </span>
                        </button>
                      ))}
                      {filteredArtists.length === 0 && (
                        <div className={`text-center py-4 ${isDark ? 'text-gray-500' : 'text-gray-400'}`}>
                          <p className="text-xs">Sanatçı bulunamadı</p>
                        </div>
                      )}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>

            <div className={`p-3 border-t ${isDark ? 'border-dark-700' : 'border-gray-200'}`}>
              <div className="flex items-center gap-2">
                <button
                  onClick={toggleTheme}
                  className={`flex-1 py-2.5 rounded-xl text-sm font-medium transition-all ${
                    isDark
                      ? 'bg-dark-700 text-gray-300 hover:bg-dark-600'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  {isDark ? '☀️ Aydınlık' : '🌙 Karanlık'}
                </button>
{isAuthenticated && (
                   <button
                     onClick={async () => { await logout(); onLogout && onLogout(); }}
                     className={`py-2.5 px-3 rounded-xl text-sm font-medium transition-all flex items-center gap-1.5 ${
                       isDark ? 'bg-dark-700 text-red-400 hover:bg-dark-600' : 'bg-gray-100 text-red-500 hover:bg-gray-200'
                     }`}
                     title="Çıkış Yap"
                   >
                     <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                       <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                     </svg>
                     <span className="hidden sm:inline">Çıkış</span>
                   </button>
                 )}
                <button
                  onClick={onReset}
                  className={`flex-1 py-2.5 rounded-xl text-sm font-medium transition-all ${
                    isDark
                      ? 'bg-dark-700 text-red-400 hover:bg-dark-600'
                      : 'bg-gray-100 text-red-500 hover:bg-gray-200'
                  }`}
                >
                  🔄 Sıfırla
                </button>
              </div>
            </div>
          </motion.aside>
        </>
      )}
    </AnimatePresence>
  );
};

export default Sidebar;