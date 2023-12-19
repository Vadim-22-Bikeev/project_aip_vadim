def calculator_1(age:int,hight:int,wight:int,life_style,gender:str):
"""Calculates the total calorie requirement to maintain weight
:param age: age of a person
:type age: int
:param hight: height of a person
:type hight: int
:param wight: weight of a person
:type wight: int
:param life_style: the level of physical activity
:type life_style: str
:param gender: gender of a person
:type gender: str
:return: the total calorie requirement to maintain weight
:rtype: int
"""

def calculate_macros( age:int,hight:int,wight:int,life_style,gender:str,goal:str):
"""Calculates the macronutrient distribution for a specific goal
:param age: age of a person
:type age: int
:param hight: height of a person
:type hight: int
:param wight: weight of a person
:type wight: int
:param life_style: the level of physical activity
:type life_style: str
:param gender: gender of a person
:type gender: str
:param goal: goal of nutrition (gain, loss, balance)
:type goal: str
:return: the distribution of macronutrients
:rtype: str
"""


def consumed_now(pr_wight,pr_cal,pr_prot,pr_fat,pr_carb):
"""Calculates the total amount of calories, protein, fat, and carbohydrates consumed based on the weight and nutritional values of a food product
:param pr_wight: the weight of the food product in grams
:type pr_wight: int
:param pr_cal: the calorie content of the food product per 100 grams
:type pr_cal: int
:param pr_prot: the protein content of the food product per 100 grams
:type pr_prot: int
:param pr_fat: the fat content of the food product per 100 grams
:type pr_fat: int
:param pr_carb: the carbohydrate content of the food product per 100 grams
:type pr_carb: int
:return: a tuple containing the total calories, protein, fat, and carbohydrates consumed
:rtype: tuple
"""


def difference(vals_r, vals_f):
    """
    Returns the difference between the values vals_f and vals_r which shows how much he has gained in calories

    :param vals_r:  The list of calculated values
    :type vals_r: list of int
    :param vals_f: The list of actual values
    :type vals_f: list of int
    :return: The list is the difference between vals_f and vals_r
    :rtype: list of list
    """