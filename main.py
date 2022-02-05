from email import message
from html.entities import html5
import logging
from pydoc import html
from queue import Empty
from subprocess import call
from aiogram import Bot, Dispatcher, executor, types

import random

from aiogram.types import reply_keyboard

import markup as nav
import media as photo

TOKEN = "5072998281:AAHG4uXYuSUdOlP1DHBh8GtEWS5KCmDh_98"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name} \n❄️1) Морозильні скрині❄️\n❄️2) Холодильні вітрини❄️\n\
❄️3) Морозильні скрині для вагового морозива❄️\n❄️4) Кондитерські холодильні вітрини❄️\n❄️5) Шафи❄️\n\
❄️6) Торговельне обладнання❄️\n❄️7) Комплектуючі❄️\n❄️8) Обладнання зі знижкою❄️'.format(message.from_user), reply_markup=nav.chooseButtons1)

@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if (callback_query.data == 'inlineButton1'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині', reply_markup=nav.chooseInlineButtons2)
        except Exception as inlineButton1:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton1)

    elif (callback_query.data == 'inlineButton2'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Холодильні вітрини', reply_markup=nav.chooseInlineButtons3)
        except Exception as inlineButton2:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton2)

    elif (callback_query.data == 'inlineButton3'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині для вагового морозива', reply_markup=nav.chooseInlineButtons4)
        except Exception as inlineButton3:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton3)

    elif (callback_query.data == 'inlineButton4'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Кондитерські холодильні вітрини')
        except Exception as inlineButton4:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton4)

    elif (callback_query.data == 'inlineButton5'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Шафи', reply_markup=nav.chooseInlineButtons5)
        except Exception as inlineButton5:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton5)

    elif (callback_query.data == 'inlineButton6'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Торговельне обладнання')
        except Exception as inlineButton6:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton6)

    elif (callback_query.data == 'inlineButton7'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Комплектуючі')
        except Exception as inlineButton7:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton7)

    elif (callback_query.data == 'inlineButton8'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Обладнання зі знижкою')
        except Exception as inlineButton8:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton8)

    elif (callback_query.data == 'inlineButton9'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині з гнутим склом "прикасові"', reply_markup=nav.chooseInlineButtons6)
        except Exception as inlineButton9:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton9)

    elif (callback_query.data == 'inlineButton10'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Cкрині з гнутим склом серії S', reply_markup=nav.chooseInlineButtons7)
        except Exception as inlineButton10:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton10)

    elif (callback_query.data == 'inlineButton11'): 
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині з гнутим склом серії SF', reply_markup=nav.chooseInlineButtons8)
        except Exception as inlineButton11:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton11)

    elif (callback_query.data == 'inlineButton12'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині з прямим склом', reply_markup=nav.chooseInlineButtons9)
        except Exception as inlineButton12:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton12)

    elif (callback_query.data == 'inlineButton13'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині з глухою кришкою', reply_markup=nav.chooseInlineButtons10)
        except Exception as inlineButton13:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton13)

    elif (callback_query.data == 'inlineButton14'):
        try:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Морозильні скрині - бонетного типу', reply_markup=nav.chooseInlineButtons11)
        except Exception as inlineButton14:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton14)

    elif (callback_query.data == 'inlineButton34'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media1)
        except Exception as inlineButton34:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton34)

    elif (callback_query.data == 'inlineButton35'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media2)
        except Exception as inlineButton35:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton35)

    elif (callback_query.data == 'inlineButton36'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media3)
        except Exception as inlineButton36:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton36)

    elif (callback_query.data == 'inlineButton37'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media4)
        except Exception as inlineButton37:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton37)

    elif (callback_query.data == 'inlineButton38'):
        try: 
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media5)
        except Exception as inlineButton38:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton38)

    elif (callback_query.data == 'inlineButton39'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media6)
        except Exception as inlineButton39:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton39)

    elif (callback_query.data == 'inlineButton40'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media7)
        except Exception as inlineButton40:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton40)

    elif (callback_query.data == 'inlineButton41'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media8)
        except Exception as inlineButton41:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton41)

    elif (callback_query.data == 'inlineButton42'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media9)
        except Exception as inlineButton42:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton42)

    elif (callback_query.data == 'inlineButton43'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media10)
        except Exception as inlineButton43:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton43)
    elif (callback_query.data == 'inlineButton44'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media11)
        except Exception as inlineButton44:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton44)

    elif (callback_query.data == 'inlineButton45'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media12)
        except Exception as inlineButton45:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton45)

    elif (callback_query.data == 'inlineButton46'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media13)
        except Exception as inlineButton46:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton46)

    elif (callback_query.data == 'inlineButton47'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media14)
        except Exception as inlineButton47:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton47)

    elif (callback_query.data == 'inlineButton48'):
        try:
            await types.ChatActions.upload_photo()
            await bot.send_media_group(callback_query.from_user.id, media=photo.media15)
        except Exception as inlineButton48:
            await types.ChatActions.typing()
            await bot.send_message(callback_query.from_user.id, 'Нажаль, дана інформація недоступна.')
            print(inlineButton48)

        


@dp.message_handler()
async def bot_message(message: types.Message):
    if(message.text == 'Рандомное число'):
        await bot.send_message(message.from_user.id, '<b>Ваше число:</b> ' + str(random.randint(1000, 9999)), parse_mode='HTML')
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)