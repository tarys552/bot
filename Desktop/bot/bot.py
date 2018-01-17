# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='513087335:AAEVOw4bLsAFNFIZZFFVitV-qo5t0iFBt4k') # Токен API к Telegram
dispatcher = updater.dispatcher

# Обработка команд
def startCommand(bot, update):
    bot.KeyboardButton(text='Запрос на определение местоположения', request_contact=None, request_location=None, **kwargs)
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')    

def textMessage(bot, update):
    response = 'Получил Ваше juj сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()

