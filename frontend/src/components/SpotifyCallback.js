import React, { useEffect, useState } from 'react';
import api from '../services/api';

const SpotifyCallback = () => {
  const [status, setStatus] = useState('loading');
  const [error, setError] = useState('');

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const code = params.get('code');
    const spotifyError = params.get('error');
    const userId = localStorage.getItem('muzikbot-spotify-user-id') || localStorage.getItem('muzikbot-auth-id') || localStorage.getItem('muzikbot-user-id');

    if (spotifyError) {
      setStatus('error');
      setError('Spotify bağlantısı reddedildi.');
      return;
    }

    if (!code) {
      setStatus('error');
      setError('Spotify callback kodu bulunamadı.');
      return;
    }

    if (!userId) {
      setStatus('error');
      setError('Kullanıcı oturumu bulunamadı. Lütfen tekrar giriş yapın.');
      return;
    }

    const redirectUri = `${window.location.origin}/spotify-callback`;

    api.post('/api/auth/spotify-callback', {
      code,
      user_id: userId,
      redirect_uri: redirectUri,
    })
      .then((response) => {
        if (response.data.spotify_connected) {
          setStatus('success');
          if (window.opener) {
            window.opener.postMessage({ type: 'spotify-connected' }, '*');
          }
          setTimeout(() => {
            window.close();
          }, 2000);
        } else {
          setStatus('error');
          setError(response.data.error || 'Spotify bağlantısı başarısız.');
        }
      })
      .catch((err) => {
        setStatus('error');
        setError(err.response?.data?.error || 'Spotify bağlantı hatası.');
      });
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#1DB954]/10 to-black/90">
      <div className="max-w-md w-full p-8 rounded-2xl bg-dark-800 border border-dark-600 text-center">
        {status === 'loading' && (
          <>
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-[#1DB954]/20 flex items-center justify-center">
              <div className="w-8 h-8 border-2 border-[#1DB954] border-t-transparent rounded-full animate-spin" />
            </div>
            <h2 className="text-xl font-bold text-white mb-2">Spotify Bağlanıyor...</h2>
            <p className="text-gray-400 text-sm">Lütfen bekleyin, hesabınız bağlanıyor.</p>
          </>
        )}

        {status === 'success' && (
          <>
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-[#1DB954]/20 flex items-center justify-center">
              <svg className="w-8 h-8 text-[#1DB954]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h2 className="text-xl font-bold text-white mb-2">Bağlantı Başarılı!</h2>
            <p className="text-gray-400 text-sm mb-4">Spotify hesabınız başarıyla bağlandı.</p>
            <p className="text-gray-500 text-xs">Bu pencere otomatik kapanacak...</p>
          </>
        )}

        {status === 'error' && (
          <>
            <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-red-500/20 flex items-center justify-center">
              <svg className="w-8 h-8 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </div>
            <h2 className="text-xl font-bold text-white mb-2">Bağlantı Hatası</h2>
            <p className="text-red-400 text-sm mb-4">{error}</p>
            <button
              onClick={() => window.close()}
              className="px-6 py-2.5 rounded-xl text-sm font-medium bg-dark-700 text-gray-300 hover:bg-dark-600 border border-dark-500"
            >
              Pencereyi Kapat
            </button>
          </>
        )}
      </div>
    </div>
  );
};

export default SpotifyCallback;