import os
from dotenv import load_dotenv

load_dotenv()

from app import serve_production

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    serve_production(port=port)