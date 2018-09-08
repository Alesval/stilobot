from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler
from uuid import uuid4
import logging

TOKEN = "621603407:AAGUCG4KNLk1rFfu3sbQNEIugQU2QfPfQJQ"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update {} caused error {}'.format(update, error))


def to_poero(query):
        string2 = ''
        for letter in query:
            if len(string2) % 2 == 0:
                string2 += letter.upper()
            else:
                string2 += letter
        return string2


def to_bold(query):
    return ('<b>' + query + '</b>')


def to_italic(query):
    return ('<i>' + query + '</i>')


def on_inline(bot, update):
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title='italic',
            input_message_content=InputTextMessageContent(message_text= to_italic(query), parse_mode='HTML')
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title='bold',
            input_message_content=InputTextMessageContent(message_text= to_bold(query), parse_mode='HTML')
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title='pOèRo',
            input_message_content=InputTextMessageContent(message_text= to_poero(query), parse_mode='HTML')
        )
    ]
    update.inline_query.answer(results)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(InlineQueryHandler(on_inline))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    print("Listening")
    updater.idle()

if __name__ == '__main__':
    main()
