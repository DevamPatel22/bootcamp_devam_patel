import os
from pathlib import Path

from dotenv import load_dotenv


def load_env():
    """Load environment variables from the local .env file."""
    load_dotenv()


def get_key(name, default=None):
    """Return an environment variable by name."""
    return os.getenv(name, default)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / get_key("DATA_DIR", "data")