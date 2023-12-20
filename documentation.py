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

    def new_str(self, id: str, value: list[str]) -> None:

        '''Adding a row to a table
        \nlist[str] - values of all columns except id
        \nIt looks like ['col_1', 'col_2', 'col_3', .......]

        :param id: the unique identifier of the string
        :type id: str
        :param value: column values other than id
        :type value: list[str]
        :return: None
        :rtype: None
        '''


    def del_str(self, id: str) -> None:

'''Deletes a row from the table by its id.

:param id: Line ID
:type id: str
:return: None
'''    

def del_str_special(self, datas: str, user_id: str) -> None:

'''Special deletion of a row with a specific date and id for the status table.

:param datas: Date of the line
:type datas: str
:param user_id: User ID
:type user_id: str
:return: None
'''

def change_one_str(self, id: str, col: str, value: str) -> None:

'''Replaces one element from one column in a row by its id.

:param id: Line ID
:type id: str
:param col: Column name
:type col: str
:param value: The new value of the element
:type value: str
:return: None
'''


def change_full_str(self, id: str, value: list) -> None:
"""Replacing all elements in a row by its id (except the id itself)

:param self: class object
:type self: object
:param id: line id
:type id: str
:param value: values of all columns except id
:type value: list[str]
:return: None
:rtype: None
"""



def show_col(self, cols: list[str]) -> list:
"""Returns all elements of columns(columns) by their names

:param self: class object
:type self: object
:param cols: a list of the names of the necessary columns
:type cols: list[str]
:return: list of column elements
:rtype: list
"""


