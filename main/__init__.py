#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID =17998867
API_HASH ="f66de5165eaa46f7f4cc5387b500d91d"
BOT_TOKEN ="5436556142:AAE8G9FXPdSpm-Y3pFjX8NiygSlpn8qnsx0"
SESSION ="AgAbF4gxodmtUJBJ3o1_733a8YjTal-wPDL38D6xICppHfKl71Hjz8tEV4fACJ7dTOli-g9jjuBG0PHyfDgG3MJ4af0onAp0n7LdaNIBgEdqnmfP-FCTUE6mfkjK7mCOQAs5CK3vrKlI2Q2oOsHYLmW-Ri_qoj2j3nWNLEb0U4hu9d40MFyTtdILZxxSjehWLdwP8ls8asgJpU2INwzTbZehZoTZNUlRjvRo-2I50VOzwX9w30-_-j5r7jBNsMnOsaJ_fC7mzc9kLJIjVGI2FTgFHHc5G2U-xWe8SqaBjazOmodIUxUecXCcUpYRIhPPQ1e1MRCbh1t2uVW4_6galq5MAAAAATZFMJAA"
FORCESUB = None
AUTH =5205471376

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
