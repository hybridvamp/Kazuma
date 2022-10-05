import os
import logging
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SUDOLIST = os.environ.get("SUDOLIST", "")
    DATABASE = os.environ.get("DATABASE")

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)