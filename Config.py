import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    FORCE_SUB1 = os.environ.get("FORCE_SUB1", "bryllbots") if os.environ.get("FORCE_SUB") else print("please add the group/channel name in env in heroku")
    FORCE_SUB2 = os.environ.get("FORCE_SUB2", "bryll_education") if os.environ.get("FORCE_SUB") else print("please add the group/channel name in env in heroku")

