import logging
from aiogram import Bot, Dispatcher, executor, types
from weatherBotClient import weatherBotClient
import os
from gettext import gettext as _
import gettext

API_TOKEN = os.getenv("botapiKey")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def initSettings():
    global logger, dp, WeatherBot
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    WeatherBot = weatherBotClient()
    gettext.install('messages', 'D:\\pyCharmProjects\\locales', ['en', 'uk'])
    gettext.bindtextdomain('messages', 'D:\\pyCharmProjects\\locales')

@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    os.environ['LANGUAGE'] = message.from_user.locale.language
    button_text = message.text
    logger.debug('The answer is %r', button_text)
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    btns_text = (_('Weather in: Bucharest'), _('Weather in: Odesa'))
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))


    await message.reply(_("Hello"), reply_markup=keyboard_markup)

@dp.message_handler()
async def all_msg_handler(message: types.Message):
    os.environ['LANGUAGE'] = message.from_user.locale.language
    button_text = message.text
    logger.debug('The answer is %r', button_text)
    if button_text == _('Weather in: Bucharest'):
        data = WeatherBot.retrieve_weather(city="Bucharest")
        reply_text = data.translateData()
    elif button_text == _('Weather in: Odesa'):
        data = WeatherBot.retrieve_weather(city="Odesa")
        reply_text = data.translateData()
    else:
        reply_text = _("Not added func")

    await message.reply(reply_text)


def initStartup():
    initSettings()
    executor.start_polling(dp, skip_updates=True)
