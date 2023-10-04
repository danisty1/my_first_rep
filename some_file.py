from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import requests

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '6561953091:AAGTiy6Q2S9LhuVkZ1IKtiuErab11TQZ64I'

# Запрос на погодный сервис
city = 'Тамбов'
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
weather_data = requests.get(url).json()
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут mark-2!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

# Этот хендлер будет срабатывать на команду "/weather"
@dp.message(Command(commands=['weather']))
async def process_weather_command(message: Message):
    await message.answer(f"В городе {city}: сейчас {str(temperature)} градусов, ощущается как {str(temperature_feels)}")

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)