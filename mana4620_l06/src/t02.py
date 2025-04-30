"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-06-21"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
from List_linked import List


# For this testing you must first complete the index method
file_variable = open("foods.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

for value in foods:
    new_list.append(value)

print(new_list.index(foods[1]))
