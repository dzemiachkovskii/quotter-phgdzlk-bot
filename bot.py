import os
from telebot import TeleBot
from image import getimg
from TOKEN import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)


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
        bot.send_photo(chat_id=m.chat.id, photo=im, caption=f"#цитата ({quote[2][2:]})")
        bot.delete_message(chat_id=m.chat.id, message_id=m.message_id)


bot.infinity_polling()
