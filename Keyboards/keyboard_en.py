from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup([
        [KeyboardButton("Content management 🔉")],
        [KeyboardButton("Statistics 📊"), KeyboardButton("Security 🛡️")],
        [KeyboardButton("Channel settings 📣"), KeyboardButton("Guide 📝")],
    ], resize_keyboard=True)

chennel_settings_menu =  InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Channels 📢", switch_inline_query_current_chat = "list_of_channels")],
        [InlineKeyboardButton("add channel ➕", callback_data = "add_channel")],
        [InlineKeyboardButton("remove channel ➖", callback_data = "remove_channel")]
    ]
)