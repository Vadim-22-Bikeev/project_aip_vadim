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
calc_PFC = InlineKeyboardButton(
    text='Расчет БЖУ',
    callback_data = 'PFC')

# Создаем объект инлайн-клавиатуры
keyboard_PFC = InlineKeyboardMarkup(
    inline_keyboard=[[calc_PFC]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.callback_query(F.data == 'new_day')
async def norm_pfc(callback: CallbackQuery):
    await callback.answer(
        text='Нажмите на кнопку:',
        reply_markup = keyboard_PFC)
if __name__ == '__main__':
    dp.run_polling(bot)