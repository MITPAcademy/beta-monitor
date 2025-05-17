import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1373355400706916352
DISCLOUD_TOKEN = os.getenv("DISCLOUD_TOKEN")
DISCLOUD_APP_ID = os.getenv("DISCLOUD_APP_ID")
DEFAULT_LANG = "en"

DISCLOUD_API = f"https://api.discloud.app/v2/app/{DISCLOUD_APP_ID}"
HEADERS = {"Authorization": DISCLOUD_TOKEN}