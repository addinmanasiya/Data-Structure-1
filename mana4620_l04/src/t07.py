"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""
# Imports

from Food_utilities import read_foods
from utilities import list_test

file = open("foods.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)
