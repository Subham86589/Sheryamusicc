import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "27469215"))
API_HASH = getenv("API_HASH", "544b135cbf33923fed1a7c461cc95f18")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7888007184:AAE0lO6y-s3nPWPzlmIPByizDk5h9VneOVY")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://nerac90218:yzto9RqoXuyKNZ3Y@cluster0.ljcva.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002311683166))

OWNER_ID = int(getenv("OWNER_ID", 7218905176))

OWNER = int(getenv("OWNER", 7218905176))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-78e67a30-6b80-4cc3-ae5e-bedd0bbcadb5")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SONGSONG220/AnieXEricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/The_Revengers_Network")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/anime_x_aegis")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQFNtIsAvQVVZBBMMm7YMvGJvK_Zf0Z62Yoo5-QyFymP5gsSQjCPVnpe8XX4nXnxW3OJO-1DaFspJadxOVxRhXXzozoOOCEtMqWeeiFFbYwXU9bIvk0O81fvHutgfI4DEauvQ86mO-xnfZ5_BWTmuOxMKZpcH04RJQ9zgvxCSMFwBtTaogexoXxHZJuvFSOJ3_l7CutJpjpqAyyksNISDg7ORs27JZwGEjCZJNVrRjTzeQOPzFlMY9m67hAcmFp8jbLvWmLvB4149kpmbHFrMhzLAIGePMcjI72FMgfM6TuZgJIBC5dSqUt6HhoxG9d8l6klSozqXf0ziUEPC26nRxxTTsIicAAAAAGqReXhAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/z7meid.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/z7meid.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/hygnc6.jpg")
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/hygnc6.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/hygnc6.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/hygnc6.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
