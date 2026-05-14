import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTheme } from '../context/ThemeContext';
import { useAuth } from '../context/AuthContext';
import { getSpotifyAuthUrl, linkSpotify, unlinkSpotify } from '../services/api';
import api from '../services/api';

const SpotifyConnectModal = ({ isOpen, onClose, onConnected }) => {
  const { isDark } = useTheme();
  const { getUserId } = useAuth();
  const [spotifyConnected, setSpotifyConnected] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    if (isOpen) {
      checkSpotifyStatus();
    }
  }, [isOpen]);

  const checkSpotifyStatus = async () => {
    try {
      const userId = getUserId();
      const response = await api.get(`/api/auth/spotify-status?user_id=${userId}`);
      setSpotifyConnected(response.data.spotify_connected);
    } catch {
      setSpotifyConnected(false);
    }
  };

  const handleConnect = async () => {
    setLoading(true);
    setError('');
    try {
      const redirectUri = `${window.location.origin}/spotify-callback`;
      const url = await getSpotifyAuthUrl(redirectUri);
      if (url) {
        localStorage.setItem('muzikbot-spotify-user-id', getUserId());
        window.open(url, '_blank', 'width=600,height=800');
      } else {
        setError('Spotify bağlantı URL\'si alınamadı.');
      }
    } catch {
      setError('Spotify bağlantı hatası.');
    } finally {
      setLoading(false);
    }
  };

  const handleDisconnect = async () => {
    setLoading(true);
    setError('');
    try {
      const userId = getUserId();
      await unlinkSpotify(userId);
      setSpotifyConnected(false);
      setSuccess('Spotify bağlantısı kaldırıldı.');
      if (onConnected) onConnected(false);
    } catch {
      setError('Bağlantı kaldırma hatası.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const handleSpotifyCallback = (e) => {
      if (e.data && e.data.type === 'spotify-connected') {
        setSpotifyConnected(true);
        setSuccess('Spotify hesabınız başarıyla bağlandı!');
        if (onConnected) onConnected(true);
      }
    };
    window.addEventListener('message', handleSpotifyCallback);
    return () => window.removeEventListener('message', handleSpotifyCallback);
  }, [onConnected]);

  if (!isOpen) return null;

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-[70] flex items-center justify-center bg-black/60 backdrop-blur-sm"
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
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-xl bg-[#1DB954] flex items-center justify-center">
                  <svg className="w-7 h-7 text-white" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.54.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.301z"/>
                  </svg>
                </div>
                <div>
                  <h3 className={`text-lg font-bold ${isDark ? 'text-white' : 'text-gray-900'}`}>
                    Spotify Hesabı
                  </h3>
                  <p className={`text-xs ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                    Playlist'lerini Spotify'a aktar
                  </p>
                </div>
              </div>
              <button
                onClick={onClose}
                className={`p-2 rounded-lg transition-colors ${
                  isDark ? 'hover:bg-dark-700 text-gray-400' : 'hover:bg-gray-100 text-gray-500'
                }`}
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            {spotifyConnected ? (
              <div className={`rounded-xl p-4 mb-4 ${
                isDark ? 'bg-green-500/10 border border-green-500/20' : 'bg-green-50 border border-green-200'
              }`}>
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-[#1DB954] flex items-center justify-center">
                    <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <div>
                    <p className={`text-sm font-medium ${isDark ? 'text-green-300' : 'text-green-700'}`}>
                      Spotify hesabın bağlı
                    </p>
                    <p className={`text-xs ${isDark ? 'text-green-400' : 'text-green-600'}`}>
                      Playlist'lerini doğrudan Spotify'a aktarabilirsin
                    </p>
                  </div>
                </div>
              </div>
            ) : (
              <div className={`rounded-xl p-4 mb-4 ${
                isDark ? 'bg-dark-900 border border-dark-600' : 'bg-gray-50 border border-gray-200'
              }`}>
                <p className={`text-sm mb-3 ${isDark ? 'text-gray-300' : 'text-gray-700'}`}>
                  Playlist'lerini Spotify'a aktarmak için hesabını bağla:
                </p>
                <ul className={`text-xs space-y-2 ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                  <li className="flex items-start gap-2">
                    <span className="text-[#1DB954] mt-0.5">✓</span>
                    <span>Spotify'da otomatik playlist oluştur</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-[#1DB954] mt-0.5">✓</span>
                    <span>Şarkıları tek tıkla Spotify'a ekle</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-[#1DB954] mt-0.5">✓</span>
                    <span>Spotify hesabına güvenli erişim</span>
                  </li>
                </ul>
              </div>
            )}

            {error && (
              <div className={`mb-3 p-3 rounded-xl text-xs ${
                isDark ? 'bg-red-500/10 border border-red-500/20 text-red-400' : 'bg-red-50 border border-red-200 text-red-600'
              }`}>
                {error}
              </div>
            )}

            {success && (
              <div className={`mb-3 p-3 rounded-xl text-xs ${
                isDark ? 'bg-green-500/10 border border-green-500/20 text-green-400' : 'bg-green-50 border border-green-200 text-green-600'
              }`}>
                {success}
              </div>
            )}

            <div className="flex gap-2">
              {spotifyConnected ? (
                <>
                  <button
                    onClick={onClose}
                    className={`flex-1 py-2.5 rounded-xl text-sm font-medium transition-all ${
                      isDark ? 'bg-dark-700 text-gray-300 hover:bg-dark-600 border border-dark-500' : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-200'
                    }`}
                  >
                    Tamam
                  </button>
                  <button
                    onClick={handleDisconnect}
                    disabled={loading}
                    className={`py-2.5 px-4 rounded-xl text-sm font-medium transition-all ${
                      isDark ? 'bg-red-500/10 text-red-400 hover:bg-red-500/20 border border-red-500/20' : 'bg-red-50 text-red-600 hover:bg-red-100 border border-red-200'
                    }`}
                  >
                    Bağlantıyı Kaldır
                  </button>
                </>
              ) : (
                <button
                  onClick={handleConnect}
                  disabled={loading}
                  className={`w-full py-3 rounded-xl text-sm font-bold transition-all flex items-center justify-center gap-2 ${
                    loading ? 'opacity-50 cursor-not-allowed' : 'hover:shadow-lg hover:shadow-green-500/25'
                  } bg-[#1DB954] hover:bg-[#1ed760] text-white`}
                >
                  <svg className="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.54.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.301z"/>
                  </svg>
                  {loading ? 'Yönlendiriliyor...' : 'Spotify ile Bağlan'}
                </button>
              )}
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default SpotifyConnectModal;