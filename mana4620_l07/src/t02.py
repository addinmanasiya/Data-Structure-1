"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-06-27"
-------------------------------------------------------
"""
from List_linked import List

lst1 = List()

lst2 = List()

array = [22, 44, 33, 55, 11]

array2 = [22, 44, 11, 55, 11]

for value in array:
    lst1.append(value)

for value in array2:
    lst2.append(value)

print(lst1.is_identical_r(lst2))
