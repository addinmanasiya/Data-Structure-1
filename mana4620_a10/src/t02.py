"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-07-27"
-------------------------------------------------------
"""
# Imports
from List_linked import List
from Sorts_List_linked import Sorts


arr = [
    84, 66, 20, 27, 8, 12, 14, 35, 67, 29,
    6, 10, 87, 2, 93, 39, 37, 69, 49
]

a = List()

for value in arr:
    a.append(value)

Sorts.radix_sort(a)

for value in a:
    print(value, end=", ")
