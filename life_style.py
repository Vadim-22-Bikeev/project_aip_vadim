from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'
# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
# Создаем объекты инлайн-кнопок
very_low = InlineKeyboardButton(
    text='Сидячий или малополвижный',
    callback_data='PASS')
low = InlineKeyboardButton(
    text='Легкая активность 1-3 раза в неделю',
    callback_data='PASS')
middle = InlineKeyboardButton(
    text='Средняя активность 3-5 раз в неделю',
    callback_data='PASS')
hard = InlineKeyboardButton(
    text='Тренеровки каждый день ',
    callback_data='PASS')
# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[very_low],
                     [low],[middle],[hard]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Выберите ваш уровень активности:',
        reply_markup=keyboard)
if __name__ == '__main__':
    dp.run_polling(bot)