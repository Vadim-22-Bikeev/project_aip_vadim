gain_weight= InlineKeyboardButton(
    text='Набор массы',
    callback_data='gain')
balance_weight = InlineKeyboardButton(
    text='Поддержание веса',
    callback_data='balance')
loss_weight = InlineKeyboardButton(
    text='Уменьшение веса',
    callback_data='loss')
# Создаем объект инлайн-клавиатуры
keyboard_goal = InlineKeyboardMarkup(
    inline_keyboard=[[gain_weight],
                     [balance_weight],[loss_weight]])
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.callback_query(F.data =='Very_low')
@dp.callback_query(F.data =='Low')
@dp.callback_query(F.data =='Middle')
@dp.callback_query(F.data =='Hard')
async def goal(callback: CallbackQuery):
    await callback.answer(
        text='Выберите вашу цель:',
        reply_markup=keyboard_goal)
if __name__ == '__main__':
    dp.run_polling(bot)