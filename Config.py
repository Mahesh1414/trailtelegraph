import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    FORCE_SUB = os.environ.get("FORCE_SUB", "") if os.environ.get("FORCE_SUB", "") else print("please add the group/channel name in env in heroku")
