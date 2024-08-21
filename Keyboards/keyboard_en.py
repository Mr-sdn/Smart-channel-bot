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