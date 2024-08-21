from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup([
        [KeyboardButton("Content management 🔉")],
        [KeyboardButton("Statistics 📊"), KeyboardButton("Security 🛡️")],
        [KeyboardButton("Channel settings 📣"), KeyboardButton("Guide 📝")],
    ], resize_keyboard=True)

chennel_settings_menu =  InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Channels 📢", switch_inline_query_current_chat = "list_of_channels")],
        [InlineKeyboardButton("Add channel ➕", callback_data = "add_channel")],
        [InlineKeyboardButton("Remove channel ➖", callback_data = "remove_channel")]
    ]
)

Cancel_operation_menu = ReplyKeyboardMarkup([
        [KeyboardButton("Cancel operation ❌")],
    ], resize_keyboard = True, placeholder = "id or username")

setting_menu_channel = InlineKeyboardMarkup(
[
    [InlineKeyboardButton("Repeated sending time setting ⏰", callback_data = "set_time")]
]
)
async def send_menu_setting_time(time: float):

    keyboard_setting_time = InlineKeyboardMarkup([
            [InlineKeyboardButton("➖", callback_data="decrease_en"), InlineKeyboardButton(f"{time} second", callback_data="not"), InlineKeyboardButton("➕", callback_data="increase_en")],
            [InlineKeyboardButton("back ⬅️", callback_data="back_en")]
    ])
    return keyboard_setting_time