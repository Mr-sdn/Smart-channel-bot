from pyrogram import Client, filters
from pyrogram.types import Message
from Messages import en # you can import any language in Message pkg
from Keyboards import keyboard_en # you can import any keyboard in Keyboards pkg
from Database import database
from Database.database import Initial_main_table



api_id = 2907144
api_hash = "dc0938f910a323e10afc005c4ffe9a68"
bot_token =" 7304496360:AAE-S78jhEkHFDxNCa9jCgMu1c5Zd0_givs"
proxy = {
    "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",  # proxy ip
    "port": 8086}

app = Client("smart-bot-channel", api_id=api_id, api_hash=api_hash, bot_token = bot_token, proxy=proxy)


@app.on_message(filters.command(["start", "home"]) & filters.private)
async def handle_welcome(client: Client, message: Message) -> None:
    await message.reply(en["welcome"], quote=True ,reply_markup = keyboard_en.main_menu)


if __name__ == "__main__":
    Initial_main_table()
    app.run()
