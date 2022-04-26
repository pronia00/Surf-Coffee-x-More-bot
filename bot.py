import telebot

from tgbot import config

bot = telebot.TeleBot(config.TOKEN)

# AdvancedCustomFilter is for list, string filter values
class MainFilter(telebot.custom_filters.AdvancedCustomFilter):
    key='text'
    @staticmethod
    def check(message, text):
        return message.text in text

# SimpleCustomFilter is for boolean values, such as is_admin=True
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']


@bot.message_handler(is_admin=True, commands=['admin']) # Check if user is admin
def admin_rep(message):
    bot.send_message(message.chat.id, "Hi admin")

@bot.message_handler(is_admin=False, commands=['admin']) # If user is not admin
def not_admin(message):
    bot.send_message(message.chat.id, "You are not admin")

@bot.message_handler(text=['hi']) # Response to hi message
def welcome_hi(message):
    bot.send_message(message.chat.id,'You said hi')

@bot.message_handler(text=['bye ']) # Response to bye message
def bye_user(message):
    bot.send_message(message.chat.id, 'You said bye')


# Do not forget to register filters
bot.add_custom_filter(MainFilter())
bot.add_custom_filter(IsAdmin())

bot.infinity_polling(skip_pending=True)

# # filters

# #from tgbot.filters.admin_filter import AdminFilter
# from telebot.types import Message
# from telebot.custom_filters import SimpleCustomFilter

# from tgbot.models.users_model import Admin

# class AdminFilter(SimpleCustomFilter):
#     key = 'is_admin'
#     @staticmethod
#     def check(Telebot, message: Message):
#         return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']


# # handlers
# from tgbot.handlers.admin import admin_user
# from tgbot.handlers.user import hey_user

# from telebot import TeleBot
# from tgbot import config

# # I recommend increasing num_threads
# bot = TeleBot(config.TOKEN, num_threads=5)

# def register_handlers():
#     bot.register_message_handler(admin_user, commands=['hey'], is_admin=True, pass_bot=True)
#     bot.register_message_handler(hey_user, commands=['hey'], is_admin=False, pass_bot=True)
#     #bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)

# @bot.message_handler(commands=['admin']) # If user is not admin
# def not_admin(message):
#     bot.send_message(message.chat.id, "You are not admin")

# def register_filters():
#     bot.add_custom_filter(AdminFilter())

# register_handlers()
# register_filters()


# # # Middlewares
# # bot.register_middleware_handler(antispam_func, update_types=['message'])


# # custom filters
# #bot.add_custom_filter(AdminFilter())



# def run():

#     bot.infinity_polling()


# run()
