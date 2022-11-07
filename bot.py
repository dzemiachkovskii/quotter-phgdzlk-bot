import os
from flask import Flask, request
from telebot import TeleBot, types
from image import getimg

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(m):
    msg = f"Привет, {m.from_user.first_name}!"
    msg += "\nОтправь текст цитаты в формате:"
    msg += "\n\n@цитата\nТекст цитаты\nАвтор цитаты"
    bot.send_message(m.chat.id, msg)


@bot.message_handler(content_types=['text'])
def txt_handler(m):
    if "@цитата" in m.text:
        quote = m.text.split("\n")
        if len(quote) < 3:
            return
        im = getimg(quote)
        bot.send_photo(chat_id=m.chat.id, photo=im, caption="#цитата")


@server.route(f'/{BOT_TOKEN}', methods=['POST'])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


APP_URL = os.environ.get('APP_URL')
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
