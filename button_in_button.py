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
man = InlineKeyboardButton(
    text='Мужчина',
    callback_data='man')
woman = InlineKeyboardButton(
    text='Женщина',
    callback_data='woman')
# Создаем объект инлайн-клавиатуры
keyboard_qender = InlineKeyboardMarkup(
    inline_keyboard=[[man],
                     [woman]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.callback_query(F.data =='PFC')
async def gender(callback: CallbackQuery):
    await callback.answer(
        text='Выберите ваш пол:',
        reply_markup=keyboard_qender)
if __name__ == '__main__':
    dp.run_polling(bot)