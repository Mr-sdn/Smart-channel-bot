from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup([
        [KeyboardButton("مدیریت محتوا 🔉")],
        [KeyboardButton("آمار 📊"), KeyboardButton("امنیت 🛡️")],
        [KeyboardButton("تنظیمات کانال 📣"), KeyboardButton("راهنما 📝")]
    ], resize_keyboard=True)