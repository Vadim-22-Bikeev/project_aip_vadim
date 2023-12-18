import time
from datetime import datetime
import random
time = datetime( datetime.now().hour, datetime.now().minute)

if time.hour == <9> and time.minute == <0>:
  await bot.send_message(message.from_user.id, f'Время: {time.hour}:{time.minute}')
else:
  await bot.send_message(message.from_user.id, time)


  f = {1:'Правильное питание: употребляйте разнообразную и сбалансированную пищу, включая фрукты, овощи, злаки, белки и здоровые жиры.', 
       2:'Ограничьте потребление сахара и обработанных продуктов.',
       3:'Пейте достаточное количество воды, около 25 миллилитров на килограмм массы тела',
       4:'Занимайтесь физической активностью регулярно: ходьба, бег, плавание, йога или другие виды спорта.',
       5:'Избегайте сидячего образа жизни: часто вставайте и делайте разминку во время работы или учебы.',
       6:'Постарайтесь получать достаточно сна каждую ночь - от 7 до 9 часов.',
       7:'Проводите время на открытом воздухе каждый день.',
       8:'Не курите и избегайте пассивного курения.',
       9:'Избегайте употребления алкоголя или ограничьте его потребление.',
       10:'Поддерживайте здоровую массу тела.',
       11:'Регулярно проверяйте свою кровь.',
       12:'Избегайте стрессовых ситуаций, если это возможно.',
       13:'Помните о гигиене рук: мойте их часто и правильно.',
       14:'Не злоупотребляйте лекарствами и обращайтесь за медицинской помощью при необходимости.':
       15:'Избегайте переедания и учите свой организм слушать, когда вы на самом деле голодны и сыты.',
       16:'Постепенно отказывайтесь от вредных привычек, таких как покупка фаст-фуда, употребление газированных напитков и т.д.',
       17:'Избегайте перенапряжения глаз при работе с компьютером или другими устройствами.'}
       



import asyncio
import random
import schedule
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

TOKEN = "YOUR_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Словарь с ключами
KEYS = {
    "ключ1": "Описание 1",
    "ключ2": "Описание 2",
    "ключ3": "Описание 3"
}

# Функция для отправки сообщения с рандомным ключом
async def send_message():
    # Выбираем случайный ключ из словаря
    random_key = random.choice(list(KEYS.keys()))
    description = KEYS[random_key]
    message = f"Сегодня рекомендую вам съесть: {random_key}\n\nОписание: {description}"

    # Отправляем сообщение пользователю (замените chat_id на ваш)
    await bot.send_message(chat_id=123456789, text=message)

# Функция для планирования отправки сообщений
def schedule_messages():
    # Запланировать отправку сообщения каждый день в указанное время
    schedule.every().day.at("09:00").do(asyncio.run, send_message)
    schedule.every().day.at("13:00").do(asyncio.run, send_message)
    schedule.every().day.at("19:00").do(asyncio.run, send_message)

    # Запустить планировщик
    while True:
        schedule.run_pending()
        asyncio.sleep(1)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # Приветственное сообщение
    await message.reply("Привет! Я бот, который рекомендует что поесть.")

    # Запустить планировщик сообщений
    asyncio.create_task(schedule_messages())

# Запустить бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





import asyncio
import datetime
import schedule
from aiogram import Bot, Dispatcher, types

API_TOKEN = 'your_bot_api_token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def send_message():
    chat_id = 'your_chat_id'
    await bot.send_message(chat_id, "Пора поесть!")

def schedule_messages():
    schedule.every().day.at("08:00").do(send_message)
    schedule.every().day.at("12:00").do(send_message)
    schedule.every().day.at("18:00").do(send_message)

async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == '__main__':
    schedule_messages()
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    executor.start_polling(dp, loop=loop)