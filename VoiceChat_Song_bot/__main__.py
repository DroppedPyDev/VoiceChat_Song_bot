import requests
from pyrogram import Client as Bot

from VoiceChat_Song_bot.config import API_HASH
from VoiceChat_Song_bot.config import API_ID
from VoiceChat_Song_bot.config import BG_IMAGE
from VoiceChat_Song_bot.config import BOT_TOKEN
from VoiceChat_Song_bot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./resources/IMG_20210924_195656_362.jpg", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VoiceChat_Song_bot.modules"),
)

bot.start()
run()
