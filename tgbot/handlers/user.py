from telebot import TeleBot
from telebot.types import Message

def hey_user(message: Message, bot: TeleBot):
    
    """
    You can create a function and use parameter pass_bot.

    """
    #mes = "Hey " + message.from_user.first_name
    bot.reply_to(message.chat.id, "Hey");
    #bot.send_message(message.chat.id, "Я только что ответил на сообщение выше ?")

