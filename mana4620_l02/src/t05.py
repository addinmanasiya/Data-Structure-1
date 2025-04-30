"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-05-24"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import stack_test

file = open('foods.txt', "r")

foods = read_foods(file)

file.close()

stack_test(foods)
