import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    'admin id'  # Tg channel @getmyid_bot
]
