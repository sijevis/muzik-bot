import { initializeApp } from "firebase/app";
import {
  getAuth,
  signInWithPopup,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  GoogleAuthProvider,
  signOut as firebaseSignOut,
  onAuthStateChanged,
  updateProfile,
} from "firebase/auth";

const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY || "",
  authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN || "",
  projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID || "",
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET || "",
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID || "",
  appId: process.env.REACT_APP_FIREBASE_APP_ID || "",
};

let app = null;
let auth = null;
let googleProvider = null;
let isConfigured = false;

const requiredKeys = ["apiKey", "authDomain", "projectId"];

if (requiredKeys.every((key) => firebaseConfig[key])) {
  try {
    app = initializeApp(firebaseConfig);
    auth = getAuth(app);
    googleProvider = new GoogleAuthProvider();
    isConfigured = true;
  } catch (error) {
    console.warn("Firebase başlatma hatası:", error.message);
    isConfigured = false;
  }
}

export const isFirebaseReady = () => isConfigured;

export const signInWithGoogle = async () => {
  if (!isConfigured || !auth) {
    throw new Error("Firebase yapılandırması eksik");
  }
  try {
    const result = await signInWithPopup(auth, googleProvider);
    const idToken = await result.user.getIdToken();
    return {
      user: {
        uid: result.user.uid,
        email: result.user.email,
        displayName: result.user.displayName,
        photoURL: result.user.photoURL,
      },
      idToken,
    };
  } catch (error) {
    if (error.code === "auth/popup-closed-by-user") {
      return null;
    }
    throw error;
  }
};

export const signInWithEmail = async (email, password) => {
  if (!isConfigured || !auth) {
    throw new Error("Firebase yapılandırması eksik");
  }
  const result = await signInWithEmailAndPassword(auth, email, password);
  const idToken = await result.user.getIdToken();
  return {
    user: {
      uid: result.user.uid,
      email: result.user.email,
      displayName: result.user.displayName || email.split('@')[0],
      photoURL: result.user.photoURL,
    },
    idToken,
  };
};

export const signUpWithEmail = async (email, password, displayName) => {
  if (!isConfigured || !auth) {
    throw new Error("Firebase yapılandırması eksik");
  }
  const result = await createUserWithEmailAndPassword(auth, email, password);
  if (displayName) {
    await updateProfile(result.user, { displayName });
  }
  const idToken = await result.user.getIdToken();
  return {
    user: {
      uid: result.user.uid,
      email: result.user.email,
      displayName: displayName || email.split('@')[0],
      photoURL: result.user.photoURL,
    },
    idToken,
  };
};

export const signOut = async () => {
  if (!isConfigured || !auth) return;
  await firebaseSignOut(auth);
};

export const onAuthChange = (callback) => {
  if (!isConfigured || !auth) {
    callback(null);
    return () => {};
  }
  return onAuthStateChanged(auth, callback);
};

export const getCurrentUser = () => {
  if (!isConfigured || !auth) return null;
  return auth.currentUser;
};

export const getIdToken = async () => {
  if (!isConfigured || !auth || !auth.currentUser) return null;
  return auth.currentUser.getIdToken();
};

export { auth };