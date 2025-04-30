"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-07-11"
-------------------------------------------------------
"""
from Food_utilities import get_food
from functions import hash_table


food1 = get_food()

print()
food2 = get_food()

print()
hash_table(4, [food1, food2])
