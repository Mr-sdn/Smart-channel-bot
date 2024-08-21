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
    ], resize_keyboard=True, placeholder = "id or username")

setting_menu_channel = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("تنظیم تایم ارسال مکرر ⏰", callback_data = "set_time")],
    ]
)


async def send_menu_setting_time(time: float):
    keyboard_setting_time = InlineKeyboardMarkup([
        [InlineKeyboardButton("➖", callback_data="decrease_fa"), InlineKeyboardButton(f"{time} ٍثانیه", callback_data="not"), InlineKeyboardButton("➕", callback_data="increase_fa")],
        [InlineKeyboardButton("بازگشت ⬅️", callback_data="back_fa")]
    ]),
    return keyboard_setting_time
