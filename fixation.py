fixation = InlineKeyboardButton(
    text='Записать съеденное',
    callback_data = 'fix')
 
end_day = InlineKeyboardButton(
    text='Закончить день',
    callback_data = 'end')
 
keyboard_fixation = InlineKeyboardMarkup(
    inline_keyboard=[[fixation],
                     [end_day]])
 
@dp.callback_query(F.data == 'go_goal')
async def norm_pfc(callback: CallbackQuery):
    await bot.send_message(
        chat_id=f'{callback.from_user.id}',
        text='Выберите группу продуктов:',
        reply_markup = keyboard_fixation)
    



t_1 = InlineKeyboardButton(
    text='Сладкое,в том числе сладкие напитки',
    callback_data = 'sweets')

t_2 = InlineKeyboardButton(
    text='Жиры разных типов',
    callback_data = 'fat_group')

t_3 = InlineKeyboardButton(
    text='Животные подукты',
    callback_data = 'animal')

t_4 = InlineKeyboardButton(
    text='Круппы',
    callback_data = 'group')

t_5 = InlineKeyboardButton(
    text='Свежие овощи и фрукты',
    callback_data = 'green')

t_6 = InlineKeyboardButton(
    text='Напитки без сахара',
    callback_data = 'no_sug_drink')

keyboard_fixation = InlineKeyboardMarkup(
    inline_keyboard=[[t_1],
                     [t_2],[t_3],[t_4],[t_5],[t_6]])

@dp.callback_query(F.data == 'go_fix')
async def norm_pfc(callback: CallbackQuery):
    await bot.send_message(
        chat_id=f'{callback.from_user.id}',
        text='Нажмите на кнопку:',
        reply_markup = keyboard_fixation)











    