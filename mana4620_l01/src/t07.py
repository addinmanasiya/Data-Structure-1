"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-05-18"
-------------------------------------------------------
"""
from Food_utilities import read_foods, get_vegetarian

file = open('foods.txt', "r")

foods = read_foods(file)

file.close()

veggies = get_vegetarian(foods)

for food in veggies:
    print(food, end="\n\n")
