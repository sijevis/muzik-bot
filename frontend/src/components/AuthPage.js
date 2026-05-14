import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useAuth } from '../context/AuthContext';
import { loginUser, registerUser } from '../services/api';

const AuthPage = ({ onLogin, onGuest }) => {
  const { loginWithBackend, loginWithGoogle, firebaseAvailable } = useAuth();
  const [view, setView] = useState('login');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [displayName, setDisplayName] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    setLoading(true);

    try {
      const backendResult = await loginUser(email, password);
      if (backendResult.user) {
        await loginWithBackend(email, password);
        onLogin(backendResult.user);
      } else {
        setError(backendResult.error || 'Giriş başarısız.');
      }
    } catch (err) {
      setError(err.message || 'Bir hata oluştu.');
    } finally {
      setLoading(false);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    if (password.length < 6) {
      setError('Şifre en az 6 karakter olmalıdır.');
      return;
    }

    setLoading(true);
    try {
      const backendResult = await registerUser(email, password, displayName || email.split('@')[0]);
      if (backendResult.user) {
        setSuccess('Kayıt başarılı! Şimdi giriş yapabilirsiniz.');
        setEmail('');
        setPassword('');
        setDisplayName('');
        setTimeout(() => {
          setView('login');
          setSuccess('');
        }, 2000);
      } else {
        setError(backendResult.error || 'Kayıt başarısız.');
      }
    } catch (err) {
      setError(err.message || 'Bir hata oluştu.');
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = async () => {
    setError('');
    setLoading(true);
    try {
      const result = await loginWithGoogle();
      if (result) {
        onLogin(result);
      }
    } catch (err) {
      setError(err.message || 'Google ile giriş başarısız.');
    } finally {
      setLoading(false);
    }
  };

  const handleGuest = () => {
    onGuest();
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-gradient-to-br from-dark-950 via-dark-900 to-primary-950 p-4 overflow-y-auto">
      <div className="w-full max-w-md my-8">
        <div className="text-center mb-8">
          <div className="w-20 h-20 rounded-2xl gradient-primary flex items-center justify-center text-4xl mx-auto mb-4 shadow-lg shadow-primary-500/30">
            🎵
          </div>
          <h1 className="text-3xl font-bold text-white mb-2">DJ AI</h1>
          <p className="text-sm text-gray-400">AI Müzik Asistanı</p>
        </div>

        <div className="rounded-2xl shadow-2xl bg-dark-800 border border-dark-600 overflow-hidden">
          <div className="flex">
            <button
              onClick={() => { setView('login'); setError(''); setSuccess(''); }}
              className={`flex-1 py-3 text-sm font-semibold transition-all ${
                view === 'login'
                  ? 'text-primary-400 border-b-2 border-primary-400 bg-dark-700/50'
                  : 'text-gray-500 hover:text-gray-300 border-b-2 border-transparent'
              }`}
            >
              Giriş Yap
            </button>
            <button
              onClick={() => { setView('register'); setError(''); setSuccess(''); }}
              className={`flex-1 py-3 text-sm font-semibold transition-all ${
                view === 'register'
                  ? 'text-primary-400 border-b-2 border-primary-400 bg-dark-700/50'
                  : 'text-gray-500 hover:text-gray-300 border-b-2 border-transparent'
              }`}
            >
              Kayıt Ol
            </button>
          </div>

          <div className="p-6">
            <AnimatePresence mode="wait">
              {view === 'login' ? (
                <motion.div
                  key="login"
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 20 }}
                  transition={{ duration: 0.2 }}
                >
                  <div className="flex items-center gap-3 mb-6">
                    <div className="w-12 h-12 rounded-full gradient-primary flex items-center justify-center text-2xl">
                      👋
                    </div>
                    <div>
                      <h2 className="text-xl font-bold text-white">Tekrar Hoş Geldin!</h2>
                      <p className="text-xs text-gray-400">Hesabına giriş yap ve müziğe devam et</p>
                    </div>
                  </div>

                  {error && (
                    <div className="mb-4 px-3 py-2.5 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm flex items-center gap-2">
                      <span>⚠</span>
                      <span>{error}</span>
                    </div>
                  )}

                  {firebaseAvailable && (
                    <>
                      <button
                        onClick={handleGoogleLogin}
                        disabled={loading}
                        className="w-full mb-4 py-3 rounded-xl font-medium text-white bg-[#4285F4] hover:bg-[#3574E0] transition-all flex items-center justify-center gap-2 shadow-lg shadow-blue-500/20"
                      >
                        <svg className="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"/>
                          <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                          <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                          <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                        </svg>
                        Google ile giriş yap
                      </button>
                      <div className="flex items-center gap-3 mb-4">
                        <div className="flex-1 h-px bg-dark-600"></div>
                        <span className="text-xs text-gray-500">veya</span>
                        <div className="flex-1 h-px bg-dark-600"></div>
                      </div>
                    </>
                  )}

                  <form onSubmit={handleLogin} className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium mb-1.5 text-gray-300">
                        Email
                      </label>
                      <div className="relative">
                        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">📧</span>
                        <input
                          type="email"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          placeholder="ornek@email.com"
                          required
                          className="w-full pl-10 pr-4 py-3 rounded-xl text-sm outline-none transition-colors bg-dark-700 border border-dark-500 text-white focus:border-primary-500 placeholder-gray-500"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="block text-sm font-medium mb-1.5 text-gray-300">
                        Şifre
                      </label>
                      <div className="relative">
                        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">🔒</span>
                        <input
                          type="password"
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          placeholder="••••••"
                          required
                          minLength={6}
                          className="w-full pl-10 pr-4 py-3 rounded-xl text-sm outline-none transition-colors bg-dark-700 border border-dark-500 text-white focus:border-primary-500 placeholder-gray-500"
                        />
                      </div>
                    </div>

                    <button
                      type="submit"
                      disabled={loading}
                      className={`w-full py-3 rounded-xl font-semibold text-white transition-all ${
                        loading
                          ? 'opacity-50 cursor-not-allowed'
                          : 'gradient-primary hover:shadow-lg hover:shadow-primary-500/25 active:scale-[0.98]'
                      }`}
                    >
                      {loading ? (
                        <span className="flex items-center justify-center gap-2">
                          <svg className="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <circle cx="12" cy="12" r="10" strokeDasharray="60" strokeDashoffset="20" />
                          </svg>
                          Giriş yapılıyor...
                        </span>
                      ) : 'Giriş Yap'}
                    </button>
                  </form>

                  <div className="mt-5 text-center text-sm text-gray-400">
                    Hesabın yok mu?{' '}
                    <button
                      onClick={() => { setView('register'); setError(''); setSuccess(''); }}
                      className="text-primary-400 hover:text-primary-300 font-medium"
                    >
                      Kayıt ol
                    </button>
                  </div>
                </motion.div>
              ) : (
                <motion.div
                  key="register"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  transition={{ duration: 0.2 }}
                >
                  <div className="flex items-center gap-3 mb-6">
                    <div className="w-12 h-12 rounded-full gradient-primary flex items-center justify-center text-2xl">
                      ✨
                    </div>
                    <div>
                      <h2 className="text-xl font-bold text-white">Yeni Hesap Oluştur</h2>
                      <p className="text-xs text-gray-400">DJ AI'a hemen başla</p>
                    </div>
                  </div>

                  {error && (
                    <div className="mb-4 px-3 py-2.5 rounded-lg bg-red-500/10 border border-red-500/30 text-red-400 text-sm flex items-center gap-2">
                      <span>⚠</span>
                      <span>{error}</span>
                    </div>
                  )}

                  {success && (
                    <div className="mb-4 px-3 py-2.5 rounded-lg bg-green-500/10 border border-green-500/30 text-green-400 text-sm flex items-center gap-2">
                      <span>✓</span>
                      <span>{success}</span>
                    </div>
                  )}

                  {firebaseAvailable && (
                    <>
                      <button
                        onClick={handleGoogleLogin}
                        disabled={loading}
                        className="w-full mb-4 py-3 rounded-xl font-medium text-white bg-[#4285F4] hover:bg-[#3574E0] transition-all flex items-center justify-center gap-2 shadow-lg shadow-blue-500/20"
                      >
                        <svg className="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 01-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"/>
                          <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                          <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                          <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                        </svg>
                        Google ile kayıt ol
                      </button>
                      <div className="flex items-center gap-3 mb-4">
                        <div className="flex-1 h-px bg-dark-600"></div>
                        <span className="text-xs text-gray-500">veya</span>
                        <div className="flex-1 h-px bg-dark-600"></div>
                      </div>
                    </>
                  )}

                  <form onSubmit={handleRegister} className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium mb-1.5 text-gray-300">
                        Ad Soyad
                      </label>
                      <div className="relative">
                        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">👤</span>
                        <input
                          type="text"
                          value={displayName}
                          onChange={(e) => setDisplayName(e.target.value)}
                          placeholder="Adınızı girin"
                          className="w-full pl-10 pr-4 py-3 rounded-xl text-sm outline-none transition-colors bg-dark-700 border border-dark-500 text-white focus:border-primary-500 placeholder-gray-500"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="block text-sm font-medium mb-1.5 text-gray-300">
                        Email
                      </label>
                      <div className="relative">
                        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">📧</span>
                        <input
                          type="email"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          placeholder="ornek@email.com"
                          required
                          className="w-full pl-10 pr-4 py-3 rounded-xl text-sm outline-none transition-colors bg-dark-700 border border-dark-500 text-white focus:border-primary-500 placeholder-gray-500"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="block text-sm font-medium mb-1.5 text-gray-300">
                        Şifre
                      </label>
                      <div className="relative">
                        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500">🔒</span>
                        <input
                          type="password"
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          placeholder="••••••"
                          required
                          minLength={6}
                          className="w-full pl-10 pr-4 py-3 rounded-xl text-sm outline-none transition-colors bg-dark-700 border border-dark-500 text-white focus:border-primary-500 placeholder-gray-500"
                        />
                      </div>
                      <p className="text-[11px] mt-1.5 text-gray-500 ml-1">
                        En az 6 karakter olmalı
                      </p>
                    </div>

                    <button
                      type="submit"
                      disabled={loading}
                      className={`w-full py-3 rounded-xl font-semibold text-white transition-all ${
                        loading
                          ? 'opacity-50 cursor-not-allowed'
                          : 'gradient-primary hover:shadow-lg hover:shadow-primary-500/25 active:scale-[0.98]'
                      }`}
                    >
                      {loading ? (
                        <span className="flex items-center justify-center gap-2">
                          <svg className="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <circle cx="12" cy="12" r="10" strokeDasharray="60" strokeDashoffset="20" />
                          </svg>
                          Kayıt yapılıyor...
                        </span>
                      ) : 'Kayıt Ol'}
                    </button>
                  </form>

                  <div className="mt-5 text-center text-sm text-gray-400">
                    Zaten hesabın var mı?{' '}
                    <button
                      onClick={() => { setView('login'); setError(''); setSuccess(''); }}
                      className="text-primary-400 hover:text-primary-300 font-medium"
                    >
                      Giriş yap
                    </button>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>

            <div className="mt-5 pt-5 border-t border-dark-600">
              <button
                onClick={handleGuest}
                disabled={loading}
                className="w-full py-3 rounded-xl text-sm font-medium transition-all text-gray-400 hover:bg-dark-700 hover:text-gray-200 border border-dark-600 hover:border-dark-500"
              >
                🎶 Ücretsiz Dene
              </button>
              <p className="text-center text-[10px] text-gray-600 mt-2">
                Kayıt olmadan da müzik keşfedebilirsin
              </p>
            </div>
          </div>
        </div>

        <p className="text-center text-[11px] text-gray-600 mt-6">
          DJ AI v2.1 — Kişisel AI Müzik Asistanı
        </p>
      </div>
    </div>
  );
};

export default AuthPage;