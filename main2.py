from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from PIL import Image, ImageFilter

TOKEN = '5566799238:AAEX2QAuIpawKnDiKCdkQgcR1GzgxNRcgGA'
print("Bot is up")
updater = Updater(TOKEN)


def welcome(update, context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('1')], [KeyboardButton('2')], [KeyboardButton('3')]]
    context.bot.send_message(chat_id=chat.id, text='Hello! I,m foto redactorbot',
                             reply_markup=ReplyKeyboardMarkup(buttons))


def operation(update, context):
    global message
    chat = update.effectiv_chat
    operation_code = update.message.text
    if operation_code in ('1'):
        operation= ('Wait')
        rate = operation[0]
        message = f'Helow{rate}'
        context.bot.send_message(chat_id=chat.id, text=message)
        img = Image.open('picture.jpg')
        img.filter(ImageFilter.BLUR)
    elif operation_code in ('2'):
        operation = ('Wait')
        rate = operation[0]
        message = f'Helow{rate}'
        context.bot.send_message(chat_id=chat.id, text=message)
        img = Image.open('picture.jpg')
        img.filter(ImageFilter.BLUR)
    elif operation_code in ('3'):
        operation = ('Wait')
        rate = operation[0]
        message = f'Helow{rate}'
        context.bot.send_message(chat_id=chat.id, text=message)
        img = Image.open('picture.jpg')
        img.filter(ImageFilter.BLUR)

disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(MessageHandler(Filters.all, operation))

updater.start_polling()
updater.idle()