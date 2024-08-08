from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup([
        [KeyboardButton("Content management 🔉")],
        [KeyboardButton("Statistics 📊"), KeyboardButton("Security 🛡️")],
        [KeyboardButton("Channel settings 📣"), KeyboardButton("Guide 📝")],
    ], resize_keyboard=True)