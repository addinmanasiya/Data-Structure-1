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
# Imports

from Food_utilities import read_foods

fv = open("foods.txt", "r")

foods = read_foods(fv)

for i in foods:
    print(i.__str__())
    print("------------------------------")
