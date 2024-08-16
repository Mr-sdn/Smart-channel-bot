import json

fa: dict
en: dict

_messages_fa = {
    "welcome": "ورود شما به ربات باعث افتخار ماست... 🙆‍♂️\n\nبه بات هوشمند کانال خیلی خوش اومدی 🧑‍🔧🌷",
    "channel_settings": "شما می توانید با انتخاب کانال خود از قسمت **کانال ها** تنظیمات کانال خود را انجام دهید 👁️🛠️....",
    "get_channel_id": "دوست عزیزم لطفا یوزرنیم کانال را برام بفرست 🆔",
    "bot_not_admin_for_add_channel": "برای اینکه ربات بتواند عملیات متفاوتی را انجام دهد، لطفا ربات را در **کانال** خود ادمین کنید و سپس دوباره کانال را اضافه کنید 🤖",
    "username_or_id_invalid": "دوست عزیزم یوزرنیم کانال اشتباه است لطفا آن دوباره بفرست 🔄☑️",
    "channel_exist": "این کانال در حال حاضر وجود دارد لطفا مجددا امتحان کنید ⛔🔄",
    "success_adding_channel": "کانال مورد نظر با موفقیت افزوده شد ✅",
    "support_only_channel": "شما مجاز هستید فقط کانال اضافه کنید لطفا آن را دوباره بفرست 🔔",
    "success_cancel_operation": "عملیات با موفقیت لغو شد 🔕",
    "channel_dont_exist":  "این کانال در حال حاضر وجود ندارد لطفا مجددا امتحان کنید ⛔🔄"

}
_messages_en = {
    "welcome": "Your entry into the bot makes us proud 🙆‍♂️...\n\nWelcome to smart bot of the channel 🧑‍🔧🌷",
    "channel_settings": "You can set settings for your channel by selecting your channel from the **channels** section 👁️🛠️....",
    "get_channel_id": "My dear friend, please send me the username of the channel 🆔",
    "bot_not_admin_for_add_channel": "In order for the bot to perform different operations, please admin the bot to your **channel** and then add the channel again 🤖",
    "username_or_id_invalid": "My dear friend, the username of the channel is wrong, please send it again 🔄☑️",
    "channel_exist": "This channel already exists, please try again ⛔🔄",
    "success_adding_channel": "The desired channel has been successfully added ✅",
    "support_only_channel": "You are only allowed to add channel, send it again 🔔",
    "success_cancel_operation": "The operation was successfully cancelled 🔕",
    "channel_dont_exist": "This channel already dont exists, please try again ⛔🔄"
    
}


def add_language_en() -> dict:

    # add messages_fa to json file
    with open('Messages/messages_en.json', 'w', encoding='utf-8') as f:
        json.dump(_messages_en, f, ensure_ascii=False, indent=4)
    with open('Messages/messages_en.json', 'r', encoding='utf-8') as f:
        messages = json.load(f)
    return messages


def add_language_fa() -> dict:

    # add messages_en to json file
    with open('Messages/messages_fa.json', 'w', encoding='utf-8') as f:
        json.dump(_messages_fa, f, ensure_ascii=False, indent=4)
    with open('Messages/messages_fa.json', 'r', encoding='utf-8') as f:
        messages = json.load(f)
    return messages


def main():
    global en, fa
    fa = add_language_fa()
    en = add_language_en()

if __name__ != '__main__':
    main()



