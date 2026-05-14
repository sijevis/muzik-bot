import React, { useState, useRef, useEffect } from 'react';
import { motion } from 'framer-motion';
import { useTheme } from '../context/ThemeContext';
import MessageBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';

const ChatArea = ({ messages, onSendMessage, isTyping, onToggleSidebar, preferences }) => {
  const { isDark } = useTheme();
  const [input, setInput] = useState('');
  const [isMultiLine, setIsMultiLine] = useState(false);
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() && !isTyping) {
      onSendMessage(input.trim());
      setInput('');
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto';
      }
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleInput = (e) => {
    setInput(e.target.value);
    const ta = e.target;
    ta.style.height = 'auto';
    ta.style.height = Math.min(ta.scrollHeight, 120) + 'px';
    setIsMultiLine(ta.value.includes('\n') || ta.scrollHeight > 44);
  };

  return (
    <div className="flex-1 flex flex-col h-full overflow-hidden">
      <header className={`flex items-center gap-3 px-4 py-3 border-b ${
        isDark ? 'bg-dark-900 border-dark-700' : 'bg-white border-gray-200'
      }`}>
        <button
          onClick={onToggleSidebar}
          className={`p-2 rounded-lg transition-colors ${
            isDark ? 'hover:bg-dark-700 text-gray-300' : 'hover:bg-gray-100 text-gray-600'
          }`}
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        <div className="flex items-center gap-2 flex-1">
          <div className="w-8 h-8 rounded-full gradient-primary flex items-center justify-center text-sm">
            🎵
          </div>
          <div>
            <h1 className={`font-semibold text-sm ${isDark ? 'text-white' : 'text-gray-900'}`}>
              DJ AI
            </h1>
            <p className={`text-[10px] ${isDark ? 'text-green-400' : 'text-green-600'}`}>
              {isTyping ? 'Yazıyor...' : 'Çevrimiçi'}
            </p>
          </div>
        </div>
        {preferences?.liked_genres?.length > 0 && (
          <div className={`hidden sm:flex items-center gap-1.5`}>
            {preferences.liked_genres.slice(0, 3).map((g, i) => (
              <span key={i} className={`px-2 py-0.5 rounded-full text-[10px] font-medium ${
                isDark ? 'bg-primary-500/20 text-primary-300' : 'bg-primary-100 text-primary-700'
              }`}>
                {g}
              </span>
            ))}
          </div>
        )}
      </header>

      <div className={`flex-1 overflow-y-auto px-4 py-4 ${
        isDark ? 'bg-dark-950' : 'bg-gray-50'
      }`}>
        <div className="max-w-3xl mx-auto space-y-4">
          {messages.map((msg, idx) => (
            <MessageBubble key={msg.id || idx} message={msg} isDark={isDark} />
          ))}
          {isTyping && <TypingIndicator isDark={isDark} />}
          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className={`px-4 py-3 border-t ${isDark ? 'bg-dark-900 border-dark-700' : 'bg-white border-gray-200'}`}>
        <form onSubmit={handleSubmit} className="max-w-3xl mx-auto">
          <div className={`flex items-end gap-2 rounded-2xl p-2 ${
            isDark ? 'bg-dark-800 border border-dark-600' : 'bg-gray-100 border border-gray-200'
          }`}>
            <textarea
              ref={textareaRef}
              value={input}
              onChange={handleInput}
              onKeyDown={handleKeyDown}
              placeholder="Müzik öneri iste..."
              rows={1}
              disabled={isTyping}
              className={`flex-1 resize-none bg-transparent px-2 py-2 text-sm outline-none max-h-[120px] ${
                isDark ? 'text-white placeholder-gray-500' : 'text-gray-800 placeholder-gray-400'
              } ${isTyping ? 'opacity-50' : ''}`}
            />
            <button
              type="submit"
              disabled={!input.trim() || isTyping}
              className={`p-2.5 rounded-xl transition-all flex-shrink-0 ${
                input.trim() && !isTyping
                  ? 'gradient-primary text-white shadow-lg shadow-primary-500/25 hover:shadow-primary-500/40'
                  : isDark ? 'bg-dark-700 text-gray-500' : 'bg-gray-200 text-gray-400'
              }`}
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
            </button>
          </div>
          <p className={`text-center text-[10px] mt-1.5 ${isDark ? 'text-gray-600' : 'text-gray-400'}`}>
            Ruh halini, türünü veya aktiviteni yaz — DJ AI öneriyor 🎵
          </p>
        </form>
      </div>
    </div>
  );
};

export default ChatArea;