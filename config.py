from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25213780")
    API_HASH = environ.get("API_HASH", "5a282fd4d8a755b4c8407ffc6e7d06ca")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8070339150:AAFgkZHEHwGTD4B1UhIhtYtLZqjIGDVDQPQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://aamirzsx:tajmahal0@cluster0.rbt2mlh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6827413016').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
