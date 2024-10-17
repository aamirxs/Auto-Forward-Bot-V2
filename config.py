from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28555306")
    API_HASH = environ.get("API_HASH", "f1527275dd7c7965f36cf4f364999ad")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8181465356:AAGsLALKRsDSicovn5hSzyZ-qihR_1MMesw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://aamir:tajmahal0@cluster0.kwtjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8198445194').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
