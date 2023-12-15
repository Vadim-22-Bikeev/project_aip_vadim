#Для написания функции телеграмм бота, которая будет принимать от пользователя запросы о возрасте, росте, весе, образе жизни и цели, а затем возвращать БЖУ и калории на день, мы можем использовать библиотеку python-telegram-bot.В функции goal() можно добавить код для расчета БЖУ и калорий на день в соответствии с выбранным образом жизни и целью.
#Также вам нужно заменить "TOKEN" на ваш токен для телеграмм бота, который вы получите при создании бота в BotFather. Следует также добавить логику обработки ошибок и входных данных.
#Это основной шаблон функции для вашего телеграмм бота. Вы можете дополнить его другими функциями или логикой.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который поможет тебе рассчитать БЖУ и калории на день.")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите свой возраст:")
    return "age"

def age(update, context):
    age = int(update.message.text)
    context.user_data["age"] = age
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите свой рост (в см):")
    return "height"

def height(update, context):
    height = int(update.message.text)
    context.user_data["height"] = height
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите свой вес (в кг):")
    return "weight"

def weight(update, context):
    weight = int(update.message.text)
    context.user_data["weight"] = weight
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите свой образ жизни:\n1. Сидячий и малоподвижный\n2. Легкая активность (упражнения 1-3 раза в неделю)\n3. Средняя активность (тренировки 3-5 раз в неделю)\n4. Высокая активность (высокие нагрузки каждый день)")
    return "lifestyle"

def lifestyle(update, context):
    lifestyle = int(update.message.text)
    context.user_data["lifestyle"] = lifestyle
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите свою цель:")
    return "goal"

def goal(update, context):
    goal = update.message.text
    context.user_data["goal"] = goal

    # Рассчет БЖУ и калорий на день
    age = context.user_data["age"]
    height = context.user_data["height"]
    weight = context.user_data["weight"]
    lifestyle = context.user_data["lifestyle"]
    goal = context.user_data["goal"]

    # .... выполнение расчетов ....

    context.bot.send_message(chat_id=update.effective_chat.id, text="Ваши БЖУ и калории на день: ...") # Вставьте сюда расчеты

def cancel(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вы отменили запрос. Для нового запроса введите /start")

def main():
    updater = Updater(token='TOKEN', use_context=True) # Вставьте сюда ваш токен
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, age))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, height))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, weight))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, lifestyle))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, goal))
    dp.add_handler(CommandHandler("cancel", cancel))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
#В функции goal() можно добавить код для расчета БЖУ и калорий на день в соответствии с выбранным образом жизни и целью. Также вам нужно заменить "TOKEN" на ваш токен для телеграмм бота, который вы получите при создании бота в BotFather. Следует также добавить логику обработки ошибок и входных данных.

#Это основной шаблон функции для вашего телеграмм бота. Вы можете дополнить его другими функциями или логикой.
def count_calories(product, volume):
    calories = {
        'хлеб': 265,
        'молоко': 60,
        'яйцо': 75,
        'мясо': 250,
        'рыба': 200,
        'овощи': 50,
        'фрукты': 60,
        'конфеты': 420,
        'чипсы': 540
    }

    product = product.lower()

    if product in calories:
        total_calories = calories[product] * volume
        return f"Продукт: {product}, объём: {volume}, калории: {total_calories} ккал"
    else:
        return f"Продукт {product} не найден в базе данных"
#Напиши функцию  телеграмм бота ,который Принимает от пользователя запрос: возраст, рост, вес, образ жизни, цель. Выдаёт БЖУ и калории на день.Образ жизни может быть:
#Сидячий и малоподвижный, легкая активность(упражнения 1-3 раза в неделю), средняя активность ( тренировки 3-5)раз в неделю), высокая активность высокие нагрузки каждый день).Оценивает обьем потребленной пищи и дает советы , что требуется еще сьесть в зависимости от цели набор массы, сброс массы или оставление веса на старом значении
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def calculate_bmi(weight, height):
    return weight / (height * height)


def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 66 + (13.75 * weight) + (5 * height * 100) - (6.75 * age)
    else:
        bmr = 655 + (9.56 * weight) + (1.85 * height * 100) - (4.68 * age)
    return bmr


def calculate_tdee(lifestyle, bmr):
    if lifestyle.lower() == 'сидячий и малоподвижный':
        tdee = bmr * 1.2
    elif lifestyle.lower() == 'легкая активность':
        tdee = bmr * 1.375
    elif lifestyle.lower() == 'средняя активность':
        tdee = bmr * 1.55
    elif lifestyle.lower() == 'высокая активность':
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.2  # По умолчанию считаем сидячий образ жизни
    return tdee


def calculate_macros(calories, goal):
    if goal.lower() == 'набор массы':
        protein = calories * 0.3 / 4
        fat = calories * 0.3 / 9
        carbs = calories * 0.4 / 4
    elif goal.lower() == 'сброс массы':
        protein = calories * 0.4 / 4
        fat = calories * 0.3 / 9
        carbs = calories * 0.3 / 4
    else:
        protein = calories * 0.25 / 4
        fat = calories * 0.25 / 9
        carbs = calories * 0.5 / 4

    return protein, fat, carbs


def calculate_calories_per_day(weight, height, age, lifestyle, goal):
    bmr = calculate_bmr(weight, height, age)
    tdee = calculate_tdee(lifestyle, bmr)
    calories = tdee if goal.lower() == "оставление веса на старом значении" else tdee - 500
    protein, fat, carbs = calculate_macros(calories, goal)

    return calories, protein, fat, carbs


def start(update, context):
    message = "Привет! Я помогу тебе рассчитать калории и БЖУ на день.\n"
    message += "Пожалуйста, отправь мне следующую информацию:\n"
    message += "1. Возраст (в годах)\n"
    message += "2. Рост (в метрах)\n"
    message += "3. Вес (в килограммах)\n"
    message += "4. Образ жизни (сидячий и малоподвижный, легкая активность, средняя активность, высокая активность)\n"
    message += "5. Цель (набор массы, сброс массы, оставление веса на старом значении)\n"
    update.message.reply_text(message)


def calculate(update, context):
    user_data = context.user_data
    age = float(update.message.text)
    height = float(user_data['height'])
    weight = float(user_data['weight'])
    lifestyle = user_data['lifestyle']
    goal = user_data['goal']

    calories, protein, fat, carbs = calculate_calories_per_day(weight, height, age, lifestyle, goal)

    message = "Твои рекомендуемые значения на день:\n"
    message += f"Калории: {calories}\n"
    message += f"Белки: {protein} г\n"
    message += f"Жиры: {fat} г\n"
    message += f"Углеводы: {carbs} г\n"

    update.message.reply_text(message)


def main():
    # Создаем экземпляр б
#"1. Принимает от пользователя запрос: возраст, рост, вес, образ жизни, цель. Выдаёт БЖУ и калории на день.
#Подсчёт уже употреблённых калорий. Принимает продукт + объём употребления, выдаёт калории.
#По п. 1 оценивает потребление и даёт советы.
#Уведомление по времени о норме приёма пищи.
#Составление статистики потребления пищи по дням в виде таблицы
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import datetime

# функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для подсчёта калорий и БЖУ.")

# функция для обработки сообщений с запросом пользователя
def handle_message(update, context):
    message = update.message.text
    chat_id = update.effective_chat.id

    # разбиваем сообщение пользователя на параметры
    params = message.split(',')
    if len(params) != 5:
        context.bot.send_message(chat_id=chat_id, text="Неправильный формат сообщения.")
        return

    age = int(params[0])
    height = int(params[1])
    weight = int(params[2])
    lifestyle = params[3]
    goal = params[4]

    # рассчитываем БЖУ и калории на день
    bzu, calories = calculate_bzu_and_calories(age, height, weight, lifestyle, goal)

    context.bot.send_message(chat_id=chat_id, text=f"БЖУ: {bzu}, калории на день: {calories}")

# функция для обработки команды /calories
def count_calories(update, context):
    message = update.message.text
    chat_id = update.effective_chat.id

    # разбиваем сообщение пользователя на продукт и объём употребления
    params = message.split(',')
    if len(params) != 2:
        context.bot.send_message(chat_id=chat_id, text="Неправильный формат сообщения.")
        return

    product = params[0]
    volume = float(params[1])

    # рассчитываем калории
    calories = calculate_calories(product, volume)

    context.bot.send_message(chat_id=chat_id, text=f"Калории: {calories}")

# функция для подсчёта БЖУ и калорий
def calculate_bzu_and_calories(age, height, weight, lifestyle, goal):
    # рассчитываем БЖУ и калории на день
    # (здесь нужно написать логику расчёта в соответствии с предоставленными параметрами)
    bzu = ...
    calories = ...

    return bzu, calories

# функция для подсчёта калорий продукта
def calculate_calories(product, volume):
    # рассчитываем калории продукта
    # (здесь нужно написать логику расчёта калорий на основе данных о продукте)
    calories = ...

    return calories

# функция для отправки уведомления о норме приёма пищи
def send_notification(context):
    now = datetime.datetime.now()
    # проверяем текущее время и отправляем уведомление, если необходимо
    # (здесь нужно написать логику формирования уведомлений)

# функция для составления статистики потребления пищи по дням
def generate_statistics(update, context):
    # генерируем таблицу статистики по потреблению пищи
    # (здесь нужно написать логику формирования статистики)

# создаем экземпляр бота
TOKEN = "YOUR_TOKEN"
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# добавляем обработчики команд
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

calories_handler = MessageHandler(Filters.regex(r'^/calories'), count_calories)
dispatcher.add_handler(calories_handler)

statistics_handler = CommandHandler('statistics', generate_statistics)
dispatcher.add_handler(statistics_handler)

# запускаем бота
updater.start_polling()
#"1. Принимает от пользователя запрос: возраст, рост, вес, образ жизни, цель. Выдаёт БЖУ и калории на день.
#Подсчёт уже употреблённых калорий. Принимает продукт + объём употребления, выдаёт калории.
#По п. 1 оценивает потребление и даёт советы.
#Уведомление по времени о норме приёма пищи.
#Составление статистики потребления пищи по дням в виде таблицы
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Здесь необходимо указать токен вашего бота
TOKEN = 'your_telegram_token'
bot = telegram.Bot(token=TOKEN)

def start(update, context):
    """Обработчик команды /start"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я телеграм бот, который поможет тебе следить за питанием.")

def calculate_bmr(age, height, weight, lifestyle):
    """Функция для расчета БЖУ и калорий на день"""
    # Ваш код для расчета БЖУ и калорий на день

def calculate_calories(food, volume):
    """Функция для подсчета калорий продукта"""
    # Ваш код для подсчета калорий продукта

def advice(age, height, weight, lifestyle, goal):
    """Функция для оценки потребления и выдачи советов"""
    # Ваш код для оценки потребления и выдачи советов

def notify_time():
    """Функция для уведомления по времени о норме приема пищи"""
    # Ваш код для уведомления по времени о норме приема пищи

def save_food_data(food, volume):
    """Функция для сохранения данных о потреблении пищи"""
    # Ваш код для сохранения данных о потреблении пищи

def get_food_statistics():
    """Функция для получения статистики потребления пищи по дням"""
    # Ваш код для получения статистики потребления пищи по дням

def handle_message(update, context):
    """Обработчик ввода пользователя"""
    user_input = update.message.text

    # Обработка запроса пользователя
    # Ваш код для обработки запроса пользователя и вызова соответствующих функций

def main():
    """Основная функция"""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Инициализация бота
bot = telegram.Bot('YOUR_TELEGRAM_BOT_API_TOKEN')

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Для подсчета калорий напишите /calc_calories.")

# Обработчик команды /calc_calories
def calc_calories(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введите продукт и его количество:")

# Обработчик сообщений с продуктом и его количеством
def process_food_input(update, context):
    food_input = update.message.text
    # Тут нужно реализовать логику подсчета калорий для введенного продукта и количества
    # Рассчет калорий и ответ пользователю
    response = calculate_calories_for_food(food_input)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Функция подсчета калорий для введенного продукта
def calculate_calories_for_food(food_input):
    # Здесь нужно реализовать логику подсчета калорий для введенного продукта
    # Пример: парсинг пользовательского ввода, поиск калорий продукта в базе данных и т.д.
    return "Калорий для {} подсчитано: {} ккал".format(food_input, "XXX")

# Инициализация и запуск бота
def main():
    updater = Updater('YOUR_TELEGRAM_BOT_API_TOKEN', use_context=True)
    dp = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("calc_calories", calc_calories))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_food_input))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
