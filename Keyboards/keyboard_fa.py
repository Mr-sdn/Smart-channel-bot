from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup([
        [KeyboardButton("مدیریت محتوا 🔉")],
        [KeyboardButton("آمار 📊"), KeyboardButton("امنیت 🛡️")],
        [KeyboardButton("تنظیمات کانال 📣"), KeyboardButton("راهنما 📝")]
    ], resize_keyboard=True)


chennel_settings_menu =  InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("کانال ها 📢", switch_inline_query_current_chat = "list_of_channels")],
        [InlineKeyboardButton("افزودن کانال ➕", callback_data = "add_channel")],
        [InlineKeyboardButton("حذف کانال ➖", callback_data = "remove_channel")]
    ]
)

Cancel_operation_menu = ReplyKeyboardMarkup([
        [KeyboardButton("لغو عملیات ❌")],
    ], resize_keyboard=True)