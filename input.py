input_data = InlineKeyboardButton(
    text='Введите дату через пробел (год месяц день):',
    callback_data='data')
# Создаем объект инлайн-клавиатуры
keyboard_input = InlineKeyboardMarkup(
    inline_keyboard=[[input_data]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.callback_querty(F.data =='statist')
async def input(callback: CallbackQuery):
    await callback.answer(
        text='Нажмите на кнопку:',
        reply_markup=keyboard_input)
if __name__ == '__main__':
    dp.run_polling(bot)