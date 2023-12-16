def calculator_1(age:int,hight:int,wight:int,life_style,gender:str):#калькулятор,который считает суммарную норму калорий для поддержания веса
    k = {'very_low':1.2 , 'low':1.375, 'middle':1.55, 'hard':1.725}
    if gender == "man":
        norm_calories_1 = round(k[life_style]*(10*wight + 6.25*hight - 5*age + 5))
    elif gender == "woman":
        norm_calories_1 = round(k[life_style]*(10*wight + 6.25*hight - 5*age - 161))
    return norm_calories_1
#Для поддержания формы нужно есть: 0.3 белка, 0.3 жира, 0.4 углеводов.
#Для похудения нужно есть: 0.4 белка, 0.15 жира, 0.45 углеводов.
#Для набора массы нужно есть: 0.35 белка, 0.15 жира, 0.5 углеводов.
# 1 грамм жира = 9 ккал
# 1 грамм белка = 4 ккал
# 1 грамм углеводов = 4 ккал
def calculate_macros(goal, age:int,hight:int,wight:int,life_style,gender:str):
    norm_calories_1 = calculator_1(age,hight,wight,life_style,gender)
    if goal == 'gain':
        if gender == 'man':
            calories_2 = norm_calories_1 + 400
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.2 / 9
            carb = calories_2 *0.5 / 4
        elif gender == 'woman':
            calories_2 = norm_calories_1 + 250
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.2 / 9
            carb = calories_2 *0.5 / 4
    elif goal == 'loss':
        if gender == 'man':
            calories_2 = norm_calories_1 - 400
            protein = calories_2 * 0.5 / 4
            fat = calories_2 * 0.15 / 9
            carb = calories_2 *0.35 / 4
        elif gender == 'woman':
            calories_2 = norm_calories_1 - 250
            protein = calories_2 * 0.5 / 4
            fat = calories_2 * 0.15 / 9
            carb = calories_2 *0.35 / 4           
    elif goal == 'balance':
        if gender == 'man':
            calories_2 = norm_calories_1
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.3 / 9
            carb = calories_2 * 0.4 / 4
        elif gender == 'woman':
            calories_2 = norm_calories_1
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.3 / 9
            carb = calories_2 * 0.4 / 4
    return str(round(protein)), str(round(fat)), str(round(carb)), str(round(calories_2))
    
