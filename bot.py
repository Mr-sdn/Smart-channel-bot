from pyrogram import Client, filters, errors,enums
from pyrogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, CallbackQuery
from Messages import en # you can import any language in Message pkg
from Keyboards import keyboard_en # you can import any keyboard in Keyboards pkg
from Database.database import initial_main_table, check_new_user, add_new_user, initial_user_table, add_channel, check_new_channel, remove_channel, get_channels, get_time
import re
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


@app.on_message(filters.regex(r"(^Cancel operation ❌$)|(^لغو عملیات ❌$)"))
async def handle_Cancel_operation(client: Client, message: Message) -> None:
    user_id = message.chat.id
    if user_id in user_state:
        user_state.pop(user_id)
    await message.reply(en["success_cancel_operation"], reply_markup = keyboard_en.main_menu)

@app.on_message(filters.text & filters.private)
async def handle_any_text(client: Client, message: Message) -> None:
    user_id = message.chat.id
    text = message.text
    if (message_state := user_state.setdefault(user_id, False)):
        if message_state == "Waiting for add channel":
            try:
                async for member in client.get_chat_members(text, limit=1):
                    pass

                channel = await client.get_chat(text)
                channel_id = str(channel.id)

                if channel.type == enums.ChatType.CHANNEL:
                    if not await check_new_channel(user_id, channel_id):
                        await add_channel(user_id, channel_id)
                        user_state.pop(user_id)
                        await message.reply(en["success_adding_channel"], reply_markup = keyboard_en.main_menu)
                    else:
                        await message.reply(en["channel_exist"])
                else:
                    await message.reply(en["support_only_channel"])
            except errors.exceptions.forbidden_403.ChatAdminRequired:
                await message.reply(en["bot_not_admin_for_add_channel"])
            except (errors.exceptions.bad_request_400.UsernameNotOccupied, errors.exceptions.bad_request_400.UsernameInvalid,
                     errors.exceptions.bad_request_400.ChannelInvalid, errors.bad_request_400.PeerIdInvalid):
                await message.reply(en["username_or_id_invalid"])

        elif message_state == "Waiting for remove channel":
            try:
                channel = await client.get_chat(text)
                channel_id = str(channel.id)
                if not await check_new_channel(user_id, channel_id):
                    await message.reply(en["channel_dont_exist"])
                else:
                    await remove_channel(user_id, channel_id)
                    user_state.pop(user_id)
                    await message.reply(en["success_removing_channel"], reply_markup = keyboard_en.main_menu)

            except (errors.exceptions.bad_request_400.UsernameNotOccupied, errors.exceptions.bad_request_400.UsernameInvalid,
                     errors.exceptions.bad_request_400.ChannelInvalid, errors.bad_request_400.PeerIdInvalid):
                await message.reply(en["username_or_id_invalid"])


@app.on_callback_query(filters.regex(r"^remove_"))
async def handle_add_query(client: Client, query: CallbackQuery) -> None:
    result = query.data.split("_")[1]
    user_id = query.from_user.id
    if result == "channel":
        await query.message.reply(en["get_channel_id"], reply_markup = keyboard_en.Cancel_operation_menu)
        user_state[user_id] = "Waiting for remove channel"


@app.on_callback_query(filters.regex(r"^add_"))
async def handle_add_query(client: Client, query: CallbackQuery) -> None:
    result = query.data.split("_")[1]
    user_id = query.from_user.id
    if result == "channel":
        await query.message.reply(en["get_channel_id"], reply_markup = keyboard_en.Cancel_operation_menu)
        user_state[user_id] = "Waiting for add channel"


@app.on_inline_query(filters.regex(r"^list_of_channels"))
async def handle_show_channels(client: Client, query: CallbackQuery) -> None:
    user_id = query.from_user.id
    results = []
    channels_id = await get_channels(user_id)
    for chat_id in channels_id:
        try:
            chat = await client.get_chat(chat_id)
            result = InlineQueryResultArticle(
            title = chat.full_name,
            input_message_content=InputTextMessageContent(f"**settings of {chat.title} channel with id: `{chat_id}`**"),
            description=f"@{chat.username}" if chat.username else "No Username",
            reply_markup = keyboard_en.setting_menu_channel
        )
        except errors.exceptions.bad_request_400.PeerIdInvalid:
            result = InlineQueryResultArticle(
            title="no result ❌",
            input_message_content=InputTextMessageContent(f"**{en["remove_bot_admin_by_user"]}**"),
            description = en["remove_bot_admin_by_user"],
        )
            
        results.append(result)
    await query.answer(results, cache_time=1)


if __name__ == "__main__":
    initial_main_table()
    app.run()
