import React from 'react';
import { motion } from 'framer-motion';

const TypingIndicator = ({ isDark }) => (
  <motion.div
    initial={{ opacity: 0, y: 10 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -10 }}
    className="flex items-start gap-2"
  >
    <div className="w-8 h-8 rounded-full gradient-primary flex items-center justify-center text-xs flex-shrink-0 shadow-md">
      🎵
    </div>
    <div className={`message-bubble ${isDark ? 'bot-bubble-dark' : 'bot-bubble-light'}`}>
      <div className="flex items-center gap-1.5 py-1">
        <motion.span
          className={`w-2 h-2 rounded-full ${isDark ? 'bg-gray-400' : 'bg-gray-500'}`}
          animate={{ y: [0, -6, 0] }}
          transition={{ duration: 0.6, repeat: Infinity, delay: 0 }}
        />
        <motion.span
          className={`w-2 h-2 rounded-full ${isDark ? 'bg-gray-400' : 'bg-gray-500'}`}
          animate={{ y: [0, -6, 0] }}
          transition={{ duration: 0.6, repeat: Infinity, delay: 0.15 }}
        />
        <motion.span
          className={`w-2 h-2 rounded-full ${isDark ? 'bg-gray-400' : 'bg-gray-500'}`}
          animate={{ y: [0, -6, 0] }}
          transition={{ duration: 0.6, repeat: Infinity, delay: 0.3 }}
        />
      </div>
    </div>
  </motion.div>
);

export default TypingIndicator;