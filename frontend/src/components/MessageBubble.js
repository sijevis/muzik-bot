import React from 'react';
import { motion } from 'framer-motion';

const formatMessage = (content) => {
  if (!content) return '';
  let text = content;
  text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" class="underline text-primary-400 hover:text-primary-300">$1</a>');
  text = text.replace(/\n/g, '<br/>');
  return text;
};

const MessageBubble = ({ message, isDark }) => {
  const isUser = message.role === 'user';

  return (
    <motion.div
      initial={{ opacity: 0, y: 20, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.3, ease: 'easeOut' }}
      className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-1`}
    >
      {!isUser && (
        <div className="flex-shrink-0 mr-2 mt-1">
          <div className="w-8 h-8 rounded-full gradient-primary flex items-center justify-center text-xs shadow-md">
            🎵
          </div>
        </div>
      )}

      <div className={`max-w-[80%] ${isUser ? 'order-1' : ''}`}>
        <div
          className={`message-bubble ${
            isUser
              ? isDark ? 'user-bubble-dark' : 'user-bubble-light'
              : isDark ? 'bot-bubble-dark' : 'bot-bubble-light'
          }`}
        >
          <div
            className="message-text"
            dangerouslySetInnerHTML={{ __html: formatMessage(message.content) }}
          />

          {message.songs && message.songs.length > 0 && (
            <div className="mt-3 space-y-2">
              {message.songs.map((song, idx) => (
                <SongMiniCard key={idx} song={song} isDark={isDark} />
              ))}
            </div>
          )}

          {message.playlistQuestion && !message.playlist && (
            <div className={`mt-3 text-xs px-3 py-2 rounded-lg ${
              isDark ? 'bg-primary-500/10 text-primary-300' : 'bg-primary-50 text-primary-600'
            }`}>
              📋 Soru: {message.playlistQuestion.question}
            </div>
          )}
        </div>

        <div className={`text-[10px] mt-1 px-2 ${
          isUser
            ? isDark ? 'text-gray-500 text-right' : 'text-gray-400 text-right'
            : isDark ? 'text-gray-600' : 'text-gray-400'
        }`}>
          {message.timestamp
            ? new Date(message.timestamp).toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' })
            : ''}
        </div>
      </div>

      {isUser && (
        <div className="flex-shrink-0 ml-2 mt-1">
          <div className={`w-8 h-8 rounded-full flex items-center justify-center text-xs shadow-md ${
            isDark ? 'bg-dark-600 text-gray-300' : 'bg-gray-200 text-gray-600'
          }`}>
            👤
          </div>
        </div>
      )}
    </motion.div>
  );
};

const SongMiniCard = ({ song, isDark }) => (
  <motion.div
    initial={{ opacity: 0, x: -10 }}
    animate={{ opacity: 1, x: 0 }}
    className={`flex items-center gap-2.5 p-2 rounded-lg transition-colors ${
      isDark ? 'bg-dark-700/50 hover:bg-dark-600' : 'bg-white hover:bg-gray-50 shadow-sm'
    }`}
  >
    <div className={`w-9 h-9 rounded-lg flex items-center justify-center flex-shrink-0 ${
      isDark ? 'bg-dark-600' : 'bg-gray-100'
    }`}>
      {song.cover_url ? (
        <img src={song.cover_url} alt={song.name} className="w-9 h-9 rounded-lg object-cover" />
      ) : (
        <span className="text-sm">🎵</span>
      )}
    </div>
    <div className="flex-1 min-w-0">
      <p className={`text-xs font-medium truncate ${isDark ? 'text-white' : 'text-gray-800'}`}>
        {song.name || song.title}
      </p>
      <p className={`text-[10px] truncate ${isDark ? 'text-gray-400' : 'text-gray-500'}`}>
        {song.artist}
      </p>
    </div>
    <div className="flex items-center gap-1.5 flex-shrink-0">
      {song.genre_label && (
        <span className={`text-[9px] px-1.5 py-0.5 rounded-full ${
          isDark ? 'bg-primary-500/20 text-primary-300' : 'bg-primary-100 text-primary-700'
        }`}>
          {song.genre_label}
        </span>
      )}
      <a
        href={`https://open.spotify.com/search/${encodeURIComponent((song.name || '') + ' ' + (song.artist || ''))}`}
        target="_blank"
        rel="noopener noreferrer"
        className={`text-[10px] font-medium ${isDark ? 'text-green-400 hover:text-green-300' : 'text-green-600 hover:text-green-500'}`}
      >
        Spotify'da Ara
      </a>
    </div>
  </motion.div>
);

export default MessageBubble;