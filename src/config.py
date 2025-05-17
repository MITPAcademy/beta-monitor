import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))
DISCLOUD_TOKEN = os.getenv("DISCLOUD_TOKEN")
DISCLOUD_APP_ID = os.getenv("DISCLOUD_APP_ID")
DEFAULT_LANG = os.getenv("DEFAULT_LANG", "en")

DISCLOUD_API = f"https://api.discloud.app/v2/app/{DISCLOUD_APP_ID}"
HEADERS = {"Authorization": DISCLOUD_TOKEN}