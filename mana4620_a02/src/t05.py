"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-05-25"
-------------------------------------------------------
"""
from Food_utilities import read_foods, food_table, food_search

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

result = food_search(foods, 5, 0, False)

food_table(result)
