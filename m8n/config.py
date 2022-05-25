# Created By @Its_romeoo
# Copyright By M8N

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSID = int(getenv("ASSID"))
ASSNAME = getenv("ASSNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID"))
UPDATE = getenv("UPDATE", "M8N_OFFICIAL")
SUPPORT = getenv("SUPPORT", "M8N_SUPPORT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5058236569").split()))
START_PIC = getenv("START_PIC")
OWNER_USERNAME = getenv("OWNER_USERNAME")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/01fc4e48cf0e4cb89a44e.jpg")
