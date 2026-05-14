import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';

const PlaylistView = ({ playlist, isDark, onClose, onShare }) => {
  if (!playlist || !playlist.songs || playlist.songs.length === 0) return null;

  return (
    <AnimatePresence>
      <motion.div
        initial={{ y: 100, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        exit={{ y: 100, opacity: 0 }}
        transition={{ type: 'spring', damping: 25, stiffness: 200 }}
        className={`playlist-panel ${isDark ? 'playlist-panel-dark' : 'playlist-panel-light'}`}
      >
        <div className="max-w-4xl mx-auto p-4">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl gradient-primary flex items-center justify-center text-xl shadow-lg">
                🎵
              </div>
              <div>
                <h3 className={`font-bold text-lg ${isDark ? 'text-white' : 'text-gray-900'}`}>
                  Playlist
                </h3>
                <p className={`text-xs ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                  {playlist.count} şarkı
                  {playlist.preferences?.mood && ` • ${playlist.preferences.mood}`}
                  {playlist.preferences?.genres?.length > 0 && ` • ${playlist.preferences.genres.join(', ')}`}
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

          <div className="space-y-2 max-h-[50vh] overflow-y-auto pr-1">
            {playlist.songs.map((song, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.05 }}
                className={`flex items-center gap-3 p-3 rounded-xl transition-all group ${
                  isDark ? 'song-card-dark hover:bg-dark-700' : 'song-card-light hover:bg-gray-50'
                }`}
              >
                <span className={`w-6 text-center text-xs font-mono ${
                  isDark ? 'text-gray-500' : 'text-gray-400'
                } group-hover:hidden`}>
                  {index + 1}
                </span>
                <span className="hidden group-hover:block w-6 text-center text-primary-500 text-xs">
                  ▶
                </span>

                <div className={`w-11 h-11 rounded-lg flex items-center justify-center flex-shrink-0 overflow-hidden ${
                  isDark ? 'bg-dark-600' : 'bg-gray-100'
                }`}>
                  {song.cover_url ? (
                    <img src={song.cover_url} alt={song.name} className="w-11 h-11 object-cover" />
                  ) : (
                    <span className="text-lg">🎵</span>
                  )}
                </div>

                <div className="flex-1 min-w-0">
                  <p className={`text-sm font-medium truncate ${isDark ? 'text-white' : 'text-gray-800'}`}>
                    {song.name || song.title}
                  </p>
                  <p className={`text-xs truncate ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
                    {song.artist}
                    {song.album && ` • ${song.album}`}
                  </p>
                </div>

                <div className="flex items-center gap-2 flex-shrink-0">
                  {song.genre_label && (
                    <span className={`text-[10px] px-2 py-0.5 rounded-full hidden sm:inline-block ${
                      isDark ? 'bg-primary-500/15 text-primary-300' : 'bg-primary-50 text-primary-600'
                    }`}>
                      {song.genre_label}
                    </span>
                  )}
                  {song.mood && (
                    <span className={`text-[10px] px-2 py-0.5 rounded-full hidden md:inline-block ${
                      isDark ? 'bg-blue-500/15 text-blue-300' : 'bg-blue-50 text-blue-600'
                    }`}>
                      {song.mood}
                    </span>
                  )}
                  {song.duration && (
                    <span className={`text-[10px] ${isDark ? 'text-gray-500' : 'text-gray-400'}`}>
                      {song.duration}
                    </span>
                  )}
                  {song.spotify_url && song.spotify_url !== '#none' && song.spotify_url !== '' ? (
                    null
                  ) : null}
                  <a
                    href={`https://open.spotify.com/search/${encodeURIComponent((song.name || '') + ' ' + (song.artist || ''))}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className={`text-xs font-medium ${isDark ? 'text-green-400 hover:text-green-300' : 'text-green-600 hover:text-green-500'}`}
                  >
                    Spotify'da Ara
                  </a>
                </div>
              </motion.div>
            ))}
          </div>

          {playlist.songs[0]?.reason && (
            <div className={`mt-3 px-3 py-2 rounded-lg text-xs ${
              isDark ? 'bg-dark-800 text-gray-400' : 'bg-gray-50 text-gray-500'
            }`}>
              💡 Şarkılar tercihlerine göre seçildi
            </div>
          )}

          {onShare && (
            <div className="mt-3 flex gap-2">
              <button
                onClick={onShare}
                className={`flex-1 py-2.5 rounded-xl text-sm font-medium transition-all ${
                  isDark ? 'bg-primary-500/20 text-primary-300 hover:bg-primary-500/30' : 'bg-primary-50 text-primary-600 hover:bg-primary-100'
                }`}
              >
                📋 İsim Ver & Kaydet
              </button>
            </div>
          )}
        </div>
      </motion.div>
    </AnimatePresence>
  );
};

export default PlaylistView;