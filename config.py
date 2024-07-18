import os

from dotenv import load_dotenv

load_dotenv()
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_USER = os.environ.get("REDIS_USER")
REDIS_USER_PASSWORD = os.environ.get("REDIS_USER_PASSWORD")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
