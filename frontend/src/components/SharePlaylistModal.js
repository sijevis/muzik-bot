import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTheme } from '../context/ThemeContext';
import { suggestPlaylistName, exportToSpotify } from '../services/api';

const SharePlaylistModal = ({ isOpen, onClose, playlist, isDark, onSave, userId, spotifyConnected, onOpenSpotifyConnect }) => {
  const [name, setName] = useState('');
  const [suggestedName, setSuggestedName] = useState('');
  const [copied, setCopied] = useState(false);
  const [loading, setLoading] = useState(false);
  const [spotifyExporting, setSpotifyExporting] = useState(false);
  const [spotifyResult, setSpotifyResult] = useState(null);
  const [spotifyError, setSpotifyError] = useState('');

  React.useEffect(() => {
    if (isOpen && playlist?.preferences) {
      setLoading(true);
      suggestPlaylistName(playlist.preferences).then((suggested) => {
        setSuggestedName(suggested || 'Playlist');
        if (!name) setName(suggested || 'Playlist');
        setLoading(false);
      });
      setSpotifyResult(null);
      setSpotifyError('');
    }
  }, [isOpen, playlist]);

  const handleCopy = () => {
    if (!playlist?.songs) return;
    const text = playlist.songs
      .map((s, i) => `${i + 1}. ${s.name} - ${s.artist}${s.genre_label ? ` [${s.genre_label}]` : ''}`)
      .join('\n');
    const full = `${name || suggestedName}\n\n${text}`;
    navigator.clipboard.writeText(full).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  const handleSave = () => {
    onSave && onSave(name || suggestedName);
    onClose();
  };

  const handleSpotifyExport = async () => {
    if (!playlist?.songs || !userId) return;
    setSpotifyExporting(true);
    setSpotifyError('');
    setSpotifyResult(null);
    try {
      const result = await exportToSpotify(userId, name || suggestedName || 'DJ AI Playlist', playlist.songs);
      setSpotifyResult(result);
    } catch (err) {
      setSpotifyError(err.message || 'Spotify aktarım hatası');
    } finally {
      setSpotifyExporting(false);
    }
  };

  if (!playlist) return null;

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-[60] flex items-center justify-center bg-black/60 backdrop-blur-sm"
          onClick={onClose}
        >
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.9, opacity: 0 }}
            className={`w-full max-w-md rounded-2xl p-6 shadow-2xl ${
              isDark ? 'bg-dark-800 border border-dark-600' : 'bg-white border border-gray-200'
            }`}
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex items-center justify-between mb-4">
              <h3 className={`text-lg font-bold ${isDark ? 'text-white' : 'text-gray-900'}`}>
                📋 Playlist'i Kaydet
              </h3>
              <button onClick={onClose} className={`p-2 rounded-lg ${isDark ? 'hover:bg-dark-700 text-gray-400' : 'hover:bg-gray-100 text-gray-500'}`}>
                ✕
              </button>
            </div>

            <div className="mb-4">
              <label className={`block text-sm font-medium mb-1.5 ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                Playlist İsmi
              </label>
              <div className="flex gap-2">
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder={suggestedName || 'Playlist ismi...'}
                  className={`flex-1 px-4 py-2.5 rounded-xl text-sm outline-none ${
                    isDark ? 'bg-dark-700 border border-dark-500 text-white focus:border-primary-500' : 'bg-gray-50 border border-gray-200 text-gray-900 focus:border-primary-500'
                  }`}
                />
                {suggestedName && (
                  <button
                    onClick={() => setName(suggestedName)}
                    className={`px-3 py-2 rounded-xl text-xs font-medium whitespace-nowrap ${
                      isDark ? 'bg-primary-500/20 text-primary-300 hover:bg-primary-500/30' : 'bg-primary-100 text-primary-700 hover:bg-primary-200'
                    }`}
                  >
                    ✨ Öner
                  </button>
                )}
              </div>
            </div>

            <div className={`mb-4 p-3 rounded-xl max-h-40 overflow-y-auto ${
              isDark ? 'bg-dark-900 border border-dark-600' : 'bg-gray-50 border border-gray-200'
            }`}>
              <p className={`text-xs font-medium mb-2 ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                {playlist.count} şarkı
              </p>
              {playlist.songs?.slice(0, 5).map((s, i) => (
                <p key={i} className={`text-xs ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                  {i + 1}. {s.name} - {s.artist}
                </p>
              ))}
              {playlist.songs?.length > 5 && (
                <p className={`text-xs mt-1 ${isDark ? 'text-gray-500' : 'text-gray-400'}`}>
                  +{playlist.songs.length - 5} şarkı daha...
                </p>
              )}
            </div>

            {spotifyError && (
              <div className="mb-3 p-2 rounded-lg bg-red-500/10 border border-red-500/20 text-red-400 text-xs">
                {spotifyError}
              </div>
            )}

            {spotifyResult && (
              <div className="mb-3 p-2 rounded-lg bg-green-500/10 border border-green-500/20 text-green-400 text-xs">
                <p className="font-medium">{spotifyResult.message}</p>
                <p>{spotifyResult.track_count}/{spotifyResult.total_songs} şarkı eklendi</p>
                {spotifyResult.playlist_url && (
                  <a href={spotifyResult.playlist_url} target="_blank" rel="noopener noreferrer" className="underline mt-1 inline-block">
                    Spotify'da aç ↗
                  </a>
                )}
              </div>
            )}

            <div className="flex gap-2">
              <button
                onClick={handleCopy}
                className={`flex-1 py-2.5 rounded-xl text-sm font-medium transition-all ${
                  copied
                    ? 'bg-green-500/20 text-green-400 border border-green-500/30'
                    : isDark ? 'bg-dark-700 text-gray-300 hover:bg-dark-600 border border-dark-500' : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-200'
                }`}
              >
                {copied ? '✓ Kopyalandı!' : '📋 Kopyala'}
              </button>
              <button
                onClick={handleSave}
                className="flex-1 py-2.5 rounded-xl text-sm font-medium text-white gradient-primary hover:shadow-lg hover:shadow-primary-500/25 transition-all"
              >
                Kaydet
              </button>
            </div>

            {userId && spotifyConnected && (
              <button
                onClick={handleSpotifyExport}
                disabled={spotifyExporting}
                className={`w-full mt-2 py-2.5 rounded-xl text-sm font-medium transition-all flex items-center justify-center gap-2 ${
                  spotifyExporting
                    ? 'opacity-50 cursor-not-allowed'
                    : 'hover:shadow-lg'
                } bg-[#1DB954] text-white hover:bg-[#1ed760]`}
              >
                <svg className="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.54.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.301z"/>
                </svg>
                {spotifyExporting ? 'Spotify\'a aktarılıyor...' : 'Spotify\'a Aktar'}
              </button>
            )}

            {userId && !spotifyConnected && (
              <button
                onClick={onOpenSpotifyConnect}
                className={`w-full mt-2 py-2.5 rounded-xl text-sm font-medium transition-all flex items-center justify-center gap-2 ${
                  isDark ? 'bg-dark-700 text-gray-300 hover:bg-dark-600 border border-dark-500' : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-200'
                }`}
              >
                <svg className="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.54.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.301z"/>
                </svg>
                Spotify Hesabı Bağla
              </button>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default SharePlaylistModal;