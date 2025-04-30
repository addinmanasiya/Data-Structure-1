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
# Imports
from Food_utilities import read_foods, average_calories

file = open('foods.txt', "rt")

foods = read_foods(file)

file.close()

avg = average_calories(foods)

print(f"Average Calories: {avg}")
