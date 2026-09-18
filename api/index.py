import sys
import os

# Mark as Vercel serverless runtime
os.environ["VERCEL"] = "1"

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from app import app, init_db

# Ensure table exists in /tmp/repurpose_cache.db on cold start
try:
    init_db()
except Exception as e:
    print(f"init_db notice: {e}")
