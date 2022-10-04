from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

BOT_TOKEN = environ.get(BOT_TOKEN)
SUDOLIST = environ.get(SUDOLIST, 1412909688)
DATABASE = environ.get(DATABASE)