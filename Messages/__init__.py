import json

fa: dict
en: dict

_messages_fa = {
    "welcome": "ورود شما به ربات باعث افتخار ماست... 🙆‍♂️\n\nبه بات هوشمند کانال خیلی خوش اومدی 🧑‍🔧🌷"
}
_messages_en = {
    "welcome": "Your entry into the bot makes us proud 🙆‍♂️...\n\nWelcome to the smart bot of the channel 🧑‍🔧🌷"
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



