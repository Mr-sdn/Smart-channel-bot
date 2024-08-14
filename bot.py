from pyrogram import Client, filters
from pyrogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from Messages import en # you can import any language in Message pkg
from Keyboards import keyboard_en # you can import any keyboard in Keyboards pkg
from Database.database import initial_main_table, check_new_user, add_new_user, initial_user_table



api_id = 29071441
api_hash = "dc0938f910a323e10afc005c4ffe9a68"
bot_token = "2071989963:AAH_9mOgQ_YQVC-Og5p64jFg2-NGH3PbWVU"
proxy = {
    "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",  # proxy ip
    "port": 8086}

app = Client("smart-bot-channel", api_id=api_id, api_hash=api_hash, bot_token = bot_token, proxy=proxy)

user_state = {}


@app.on_message(filters.command(["start", "home"]) & filters.private)
async def handle_welcome(client: Client, message: Message) -> None:
    user_id = message.chat.id
    if not await check_new_user(user_id):
        await add_new_user(user_id)
        await initial_user_table(user_id)

    await message.reply(en["welcome"], reply_markup = keyboard_en.main_menu)


@app.on_message(filters.regex(r"(^Channel settings 📣$)|(^تنظیمات کانال 📣$)"))
async def handle_channel_settings(client: Client, message: Message) -> None:
    await message.reply(en["channel_settings"], reply_markup = keyboard_en.chennel_settings_menu)


@app.on_callback_query(filters.regex(r"^add_"))
async def handle_add_query(client: Client, query: CallbackQuery):
    result = query.data.split("_")[1]
    id = query.from_user.id
    if result == "channel":
        await query.message.reply(en["get_channel_id"], reply_markup = keyboard_en.Cancel_operation_menu)
        user_state[id] = "Waiting for the send channel"








if __name__ == "__main__":
    initial_main_table()
    app.run()
