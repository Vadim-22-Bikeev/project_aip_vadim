input_data = InlineKeyboardButton(
    text='Введите дату через пробел (год месяц день):',
    callback_data='data_way')
# Создаем объект инлайн-клавиатуры
keyboard_input = InlineKeyboardMarkup(
    inline_keyboard=[[input_data]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.callback_query(F.data == 'statist')
async def input(callback: CallbackQuery):
    await bot.send_message(
        chat_id=f'{callback.from_user.id}',
        text='Нажмите на кнопку:',
        reply_markup = keyboard_input)