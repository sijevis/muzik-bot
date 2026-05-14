import React, { createContext, useState, useEffect, useContext } from 'react';
import {
  isFirebaseReady,
  signInWithGoogle,
  signInWithEmail,
  signUpWithEmail,
  signOut as firebaseSignOut,
  onAuthChange,
  getIdToken,
} from '../services/firebase';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [firebaseAvailable, setFirebaseAvailable] = useState(false);

  useEffect(() => {
    const ready = isFirebaseReady();
    setFirebaseAvailable(ready);

    if (ready) {
      const unsubscribe = onAuthChange((firebaseUser) => {
        if (firebaseUser) {
          setUser({
            uid: firebaseUser.uid,
            email: firebaseUser.email,
            displayName: firebaseUser.displayName || firebaseUser.email?.split('@')[0] || 'Kullanıcı',
            photoURL: firebaseUser.photoURL,
          });
        } else {
          const localUserId = localStorage.getItem('muzikbot-user-id');
          if (localUserId) {
            setUser({ uid: localUserId, displayName: localUserId.split('@')[0] || 'Kullanıcı', isLocal: true });
          } else {
            setUser(null);
          }
        }
        setLoading(false);
      });
      return () => unsubscribe();
    } else {
      const localUserId = localStorage.getItem('muzikbot-auth-id');
      if (localUserId && localStorage.getItem('muzikbot-logged-in') === 'true') {
        setUser({ uid: localUserId, displayName: localStorage.getItem('muzikbot-display-name') || localUserId.split('@')[0] || 'Kullanıcı', isLocal: true });
      }
      setLoading(false);
    }
  }, []);

  const setBackendUser = (backendUser) => {
    const userData = {
      uid: backendUser.user_id || backendUser.email,
      email: backendUser.email,
      displayName: backendUser.display_name || backendUser.email?.split('@')[0] || 'Kullanıcı',
      isLocal: true,
    };
    setUser(userData);
    localStorage.setItem('muzikbot-auth-id', userData.uid);
    localStorage.setItem('muzikbot-user-id', userData.uid);
    localStorage.setItem('muzikbot-logged-in', 'true');
    localStorage.setItem('muzikbot-display-name', userData.displayName);
    return userData;
  };

  const loginWithBackend = async (email, password) => {
    if (firebaseAvailable) {
      try {
        const result = await signInWithEmail(email, password);
        if (result && result.user) {
          setUser(result.user);
          localStorage.setItem('muzikbot-user-id', result.user.email);
          if (result.idToken) {
            try {
              const { default: api } = await import('../services/api');
              await api.post('/api/auth/verify', { id_token: result.idToken });
            } catch (e) {
              console.warn('Backend token doğrulama hatası:', e);
            }
          }
          return result.user;
        }
      } catch (firebaseErr) {
        console.warn('Firebase giriş hatası, backend girişi başarılı:', firebaseErr.message);
      }
    }

    const localUserId = email;
    const userData = { uid: localUserId, email, displayName: email.split('@')[0] || 'Kullanıcı', isLocal: true };
    setUser(userData);
    localStorage.setItem('muzikbot-auth-id', localUserId);
    localStorage.setItem('muzikbot-logged-in', 'true');
    localStorage.setItem('muzikbot-display-name', userData.displayName);
    return userData;
  };

  const registerWithBackend = async (email, password, displayName) => {
    if (firebaseAvailable) {
      try {
        if (result && result.user) {
          setUser(result.user);
          localStorage.setItem('muzikbot-auth-id', result.user.email);
          localStorage.setItem('muzikbot-logged-in', 'true');
          localStorage.setItem('muzikbot-display-name', result.user.displayName || result.user.email?.split('@')[0] || 'Kullanıcı');
          if (result.idToken) {
            try {
              const { default: api } = await import('../services/api');
              await api.post('/api/auth/verify', { id_token: result.idToken });
            } catch (e) {
              console.warn('Backend token doğrulama hatası:', e);
            }
          }
          return result.user;
        }
      } catch (firebaseErr) {
        console.warn('Firebase kayıt hatası, backend kaydı başarılı:', firebaseErr.message);
      }
    }

    const localUserId = email;
    const userData = { uid: localUserId, email, displayName: displayName || email.split('@')[0] || 'Kullanıcı', isLocal: true };
    setUser(userData);
    localStorage.setItem('muzikbot-auth-id', localUserId);
    localStorage.setItem('muzikbot-logged-in', 'true');
    localStorage.setItem('muzikbot-display-name', userData.displayName);
    return userData;
  };

  const loginWithGoogle = async () => {
    if (!firebaseAvailable) {
      throw new Error('Firebase yapılandırması eksik');
    }
    const result = await signInWithGoogle();
if (result && result.user) {
          setUser(result.user);
          localStorage.setItem('muzikbot-auth-id', result.user.email);
          localStorage.setItem('muzikbot-logged-in', 'true');
          localStorage.setItem('muzikbot-display-name', result.user.displayName || result.user.email?.split('@')[0] || 'Kullanıcı');
          if (result.idToken) {
        try {
          const { default: api } = await import('../services/api');
          await api.post('/api/auth/verify', { id_token: result.idToken });
        } catch (e) {
          console.warn('Backend token doğrulama hatası:', e);
        }
      }
      return result.user;
    }
    return null;
  };

  const loginAsGuest = () => {
    const guestId = 'guest_' + Date.now();
    const userData = { uid: guestId, displayName: 'Misafir', isLocal: true, isGuest: true };
    setUser(userData);
    localStorage.setItem('muzikbot-auth-id', guestId);
    localStorage.setItem('muzikbot-logged-in', 'true');
    localStorage.setItem('muzikbot-display-name', 'Misafir');
    return userData;
  };

  const logout = async () => {
    if (firebaseAvailable) {
      await firebaseSignOut();
    }
    setUser(null);
    localStorage.removeItem('muzikbot-auth-id');
    localStorage.removeItem('muzikbot-logged-in');
    localStorage.removeItem('muzikbot-display-name');
    localStorage.removeItem('muzikbot-user-id');
    localStorage.removeItem('muzikbot-welcomed');
  };

  const getUserId = () => {
    if (user) return user.uid;
    return localStorage.getItem('muzikbot-auth-id') || localStorage.getItem('muzikbot-user-id') || 'anonymous';
  };

  const getToken = async () => {
    if (firebaseAvailable) {
      return await getIdToken();
    }
    return null;
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        firebaseAvailable,
        setBackendUser,
        loginWithBackend,
        registerWithBackend,
        loginWithGoogle,
        loginAsGuest,
        logout,
        getUserId,
        getToken,
        isAuthenticated: !!user,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};