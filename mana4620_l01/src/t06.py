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
from Food_utilities import write_foods
from Food import Food
fv = open("new_foods.txt", "w")

k = Food("Chicken Wings", 2, False, 130)
y = Food("Crotons Salad", 0, True, 500)

l = [k, y]
write_foods(fv, l)
fv.close()
