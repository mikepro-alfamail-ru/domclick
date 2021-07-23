
from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot
from requestsapi.models import Customers

import logging
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    if len(update.message.text.split(' ')) > 1:
        email = update.message.text.split(' ')[1]
        if Customers.objects.filter(email=email):
            customer = Customers.objects.filter(email=email)
            # customer.telegram = update.message.chat_id
            customer.update(telegram=update.message.chat_id)
    context.bot.sendMessage(update.message.chat_id, text='Hi!')


def help(update, context):
    context.bot.sendMessage(update.message.chat_id, text='Help!')


def echo(update, context):
    context.bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Loading handlers for telegram bot")

    # Default dispatcher (this is related to the first bot in settings.DJANGO_TELEGRAMBOT['BOTS'])
    dp = DjangoTelegramBot.dispatcher
    # To get Dispatcher related to a specific bot
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_token')     #get by bot token
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_username')  #get by bot username

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
