import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || '';

const api = axios.create({
  baseURL: API_URL,
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use(async (config) => {
  const userId = localStorage.getItem('muzikbot-auth-id') || localStorage.getItem('muzikbot-user-id');
  if (userId) {
    config.headers['X-User-Id'] = userId;
  }
  try {
    const { getIdToken } = await import('../services/firebase');
    const token = await getIdToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
  } catch {}
  return config;
});

export const sendMessage = async (message, sessionId, userId) => {
  try {
    const response = await api.post('/api/chat', {
      message,
      session_id: sessionId,
      user_id: userId || sessionId,
    });
    return response.data;
  } catch (error) {
    if (error.code === 'ECONNABORTED') {
      throw new Error('İstek zaman aşımına uğradı. Backend sunucusunun çalıştığından emin olun.');
    }
    throw new Error(
      'Bağlantı hatası! Backend sunucusunun çalıştığından emin olun:\n\n' +
      '1. Backend sunucusunu başlatın\n' +
      '2. Sunucunun çalıştığını kontrol edin\n' +
      '3. Sayfayı yenilemeyi deneyin'
    );
  }
};

export const getCategories = async () => {
  try {
    const response = await api.get('/api/categories');
    return response.data.categories || [];
  } catch {
    return [
      { label: "Playlist Yap", message: "Bana karışık playlist yap", icon: "📋" },
      { label: "Rock", message: "Bana rock müzik öner", icon: "🎸" },
      { label: "Motivasyon", message: "Motivasyona ihtiyacım var", icon: "💪" },
      { label: "Üzgünüm", message: "Moralim bozuk, ne dinleyebilirim?", icon: "😢" },
      { label: "Romantik", message: "Aşk şarkısı öner", icon: "❤️" },
      { label: "Spor / Gym", message: "Spor yaparken dinleyeceğim şarkılar öner", icon: "🏃" },
      { label: "Gece Yolculuğu", message: "Gece yolculuğunda dinleyeceğim müzik öner", icon: "🌙" },
      { label: "Lo-fi", message: "Lo-fi müzik öner", icon: "🎧" },
      { label: "Jazz", message: "Jazz müzik öner", icon: "🎷" },
      { label: "Türkçe Rock", message: "Türkçe rock öner", icon: "🎸" },
      { label: "Sakinleş", message: "Sakinleşmek istiyorum", icon: "🧘" },
      { label: "Arabesk", message: "Arabesk müzik öner", icon: "🎭" },
    ];
  }
};

export const getArtists = async () => {
  try {
    const response = await api.get('/api/artists');
    return response.data.artists || [];
  } catch {
    return [];
  }
};

export const getStatus = async () => {
  try {
    const response = await api.get('/api/status');
    return response.data;
  } catch {
    return { status: 'offline', demo_mode: true };
  }
};

export const getUserPreferences = async (userId) => {
  try {
    const response = await api.get(`/api/user/${userId}/preferences`);
    return response.data.preferences;
  } catch {
    return null;
  }
};

export const getUserPlaylists = async (userId) => {
  try {
    const response = await api.get(`/api/user/${userId}/playlists`);
    return response.data.playlists || [];
  } catch {
    return [];
  }
};

export const resetSession = async (sessionId, userId) => {
  try {
    await api.post(`/api/reset/${sessionId}`, { user_id: userId });
    return true;
  } catch {
    return false;
  }
};

export const registerUser = async (email, password, displayName) => {
  try {
    const response = await api.post('/api/auth/register', {
      email,
      password,
      display_name: displayName,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Kayıt başarısız.');
  }
};

export const loginUser = async (email, password) => {
  try {
    const response = await api.post('/api/auth/login', { email, password });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Giriş başarısız.');
  }
};

export const getPlaylistById = async (playlistId) => {
  try {
    const response = await api.get(`/api/playlist/${playlistId}`);
    return response.data;
  } catch {
    return null;
  }
};

export const renamePlaylist = async (playlistId, name) => {
  try {
    const response = await api.post(`/api/playlist/${playlistId}/rename`, { name });
    return response.data;
  } catch {
    return null;
  }
};

export const deletePlaylist = async (playlistId, userId) => {
  try {
    const response = await api.post(`/api/playlist/${playlistId}/delete`, { user_id: userId });
    return response.data;
  } catch {
    return null;
  }
};

export const suggestPlaylistName = async (preferences) => {
  try {
    const response = await api.post('/api/playlist/suggest-name', { preferences });
    return response.data.name;
  } catch {
    return null;
  }
};

export const getSpotifyAuthUrl = async (redirectUri) => {
  try {
    const response = await api.get('/api/auth/spotify-url', { params: { redirect_uri: redirectUri } });
    return response.data.url;
  } catch {
    return null;
  }
};

export const spotifyCallback = async (code, userId, redirectUri) => {
  try {
    const response = await api.post('/api/auth/spotify-callback', {
      code,
      user_id: userId,
      redirect_uri: redirectUri,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Spotify bağlantı hatası.');
  }
};

export const getSpotifyStatus = async (userId) => {
  try {
    const response = await api.get(`/api/auth/spotify-status?user_id=${userId}`);
    return response.data;
  } catch {
    return { spotify_connected: false };
  }
};

export const linkSpotify = async (userId, accessToken, refreshToken, expiresAt) => {
  try {
    const response = await api.post('/api/auth/spotify-link', {
      user_id: userId,
      access_token: accessToken,
      refresh_token: refreshToken,
      expires_at: expiresAt,
    });
    return response.data;
  } catch {
    return null;
  }
};

export const unlinkSpotify = async (userId) => {
  try {
    const response = await api.post('/api/auth/spotify-unlink', { user_id: userId });
    return response.data;
  } catch {
    return null;
  }
};

export const enrichSongs = async (songs) => {
  try {
    const response = await api.post('/api/enrich', { songs });
    return response.data.songs || songs;
  } catch {
    return songs;
  }
};

export const exportToSpotify = async (userId, playlistName, songs) => {
  try {
    const response = await api.post('/api/spotify/export-playlist', {
      user_id: userId,
      playlist_name: playlistName,
      songs,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Spotify aktarım hatası.');
  }
};

export default api;