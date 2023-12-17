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
start_countind_day = InlineKeyboardButton(
    text='Начать учет дня',
    callback_data='new_day')
view_statistics = InlineKeyboardButton(
    text='Посмотреть статистику',
    callback_data='PASS')
# Создаем объект инлайн-клавиатуры
keyboard_start = InlineKeyboardMarkup(
    inline_keyboard=[[start_countind_day],
                     [view_statistics]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Выберите опцию:',
        reply_markup=keyboard_start)
if __name__ == '__main__':
    dp.run_polling(bot)