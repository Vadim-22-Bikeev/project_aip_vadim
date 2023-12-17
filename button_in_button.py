from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

# Создание бота и диспетчера
bot = Bot(token="YOUR_TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды /start
@dp.message_handler(Command("start"))
async def start_handler(message: types.Message):
    # Создание инлайн клавиатуры
    inline_kb = types.InlineKeyboardMarkup(row_width=2)

    # Добавление кнопок в инлайн клавиатуру
    inline_btn1 = types.InlineKeyboardButton(text="Button 1", callback_data="button1")
    inline_btn2 = types.InlineKeyboardButton(text="Button 2", callback_data="button2")
    inline_btn3 = types.InlineKeyboardButton(text="Button 3", callback_data="button3")
    
    inline_kb.row(inline_btn1, inline_btn2, inline_btn3)

    # Отправка сообщения с инлайн клавиатурой
    await message.answer("Choose a button:", reply_markup=inline_kb)


# Обработчик выбора кнопки из инлайн клавиатуры
@dp.callback_query_handler(text="button1")
async def button1_handler(callback_query: types.CallbackQuery):
    # Создание и добавление кнопок во вложенную инлайн клавиатуру
    inline_kb = types.InlineKeyboardMarkup(row_width=1)
    inline_btn1 = types.InlineKeyboardButton(text="Nested Button 1", callback_data="nested_button1")
    inline_btn2 = types.InlineKeyboardButton(text="Nested Button 2", callback_data="nested_button2")
    inline_kb.row(inline_btn1, inline_btn2)

    # Изменение сообщения с вложенной инлайн клавиатурой
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=inline_kb)


# Обработчик выбора кнопки из вложенной инлайн клавиатуры
@dp.callback_query_handler(text="nested_button1")
async def nested_button1_handler(callback_query: types.CallbackQuery):
    # Обработка нажатия на первую вложенную кнопку
    await bot.answer_callback_query(callback_query.id, text="Nested Button 1 was pressed")


# Обработчик выбора кнопки из вложенной инлайн клавиатуры
@dp.callback_query_handler(text="nested_button2")
async def nested_button2_handler(callback_query: types.CallbackQuery):
    # Обработка нажатия на вторую вложенную кнопку
    await bot.answer_callback_query(callback_query.id, text="Nested Button 2 was pressed")


# Запуск бота
if __name__ == '__main__':
    dp.infinity_polling()