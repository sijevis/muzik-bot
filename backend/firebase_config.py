import os
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

FIREBASE_AVAILABLE = False
db = None
auth = None

FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "")
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH", "")

if FIREBASE_PROJECT_ID or FIREBASE_CREDENTIALS_PATH:
    try:
        import firebase_admin
        from firebase_admin import credentials, firestore as fs, auth as fb_auth

        if FIREBASE_CREDENTIALS_PATH and os.path.exists(FIREBASE_CREDENTIALS_PATH):
            cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
        elif os.path.exists(os.path.join(os.path.dirname(__file__), "firebase-credentials.json")):
            cred = credentials.Certificate(
                os.path.join(os.path.dirname(__file__), "firebase-credentials.json")
            )
        else:
            cred = credentials.ApplicationDefault()

        firebase_admin.initialize_app(cred)
        db = fs.client()
        try:
            auth = fb_auth
        except Exception:
            auth = None

        FIREBASE_AVAILABLE = True
        logger.info("Firebase basariyla baglandi")
    except ImportError:
        logger.warning("firebase-admin paketi yuklu degil. pip install firebase-admin ile yukleyin.")
        FIREBASE_AVAILABLE = False
    except Exception as e:
        logger.warning(f"Firebase baglantisi basarisiz: {e}")
        FIREBASE_AVAILABLE = False


def is_firebase_available():
    return FIREBASE_AVAILABLE


def verify_firebase_token(id_token):
    if not FIREBASE_AVAILABLE or auth is None:
        return None
    try:
        decoded = auth.verify_id_token(id_token)
        return {
            "uid": decoded["uid"],
            "email": decoded.get("email", ""),
            "name": decoded.get("name", ""),
            "picture": decoded.get("picture", ""),
        }
    except Exception as e:
        logger.warning(f"Firebase token dogrulama hatasi: {e}")
        return None


def get_firestore_client():
    return db