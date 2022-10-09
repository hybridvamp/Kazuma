import os
import logging
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


class Config:
    API_ID = int(os.environ.get("API_ID", 1234))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SUDOLIST = int(os.environ.get("SUDOLIST", 1412909688))
    DATABASE = os.environ.get("DATABASE", "")

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)