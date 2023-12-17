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
    callback_data='Very_low')
low = InlineKeyboardButton(
    text='Легкая активность 1-3 раза в неделю',
    callback_data='Low')
middle = InlineKeyboardButton(
    text='Средняя активность 3-5 раз в неделю',
    callback_data='Middle')
hard = InlineKeyboardButton(
    text='Тренеровки каждый день ',
    callback_data='Hard')
# Создаем объект инлайн-клавиатуры
keyboard_style = InlineKeyboardMarkup(
    inline_keyboard=[[very_low],
                     [low],[middle],[hard]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.callback_querty(F.data == 'PASS'))
async def style_life(callback: CallbackQuery):
    await callback.answer(
        text='Выберите ваш уровень активности:',
        reply_markup=keyboard_style)
if __name__ == '__main__':
    dp.run_polling(bot)