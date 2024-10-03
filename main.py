from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '6812644604:AAHN7f7qtMbTBKIg5mJi5n5rItpJKyyOU7s'  # Вставьте ваш токен от BotFather
WEB_APP_URL = 'https://github.com/RedBounceYT/squirrel-coin-web-app.git'  # Вставьте ссылку на ваше веб-приложение

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Отправляем сообщение с кнопкой для открытия Web App
    keyboard = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(text="Играть в Белка Коин", web_app=types.WebAppInfo(url=WEB_APP_URL))
    keyboard.add(web_app_button)

    await message.reply("Привет! Нажми на кнопку, чтобы начать игру в Белка Коин!", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
