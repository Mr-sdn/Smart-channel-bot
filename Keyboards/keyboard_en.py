from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup([
        [KeyboardButton("content management 🔉")],
        [KeyboardButton("statistics 📊"), KeyboardButton("security 🛡️")],
        [KeyboardButton("Channel settings 📣"), KeyboardButton("Guide 📝")],
    ], resize_keyboard=True)