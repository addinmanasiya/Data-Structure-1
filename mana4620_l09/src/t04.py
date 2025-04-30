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
from Hash_Set_array import Hash_Set

hset = Hash_Set(1)

arr = [100, 1000, 20, 5, 6, 10, 2, 9, 3400, 300, 500, 10000]

for value in arr:
    hset.insert(value)

print("Hash Set: ")
hset.debug()

for value in arr:
    hset.insert(value + 1)
    hset.insert(value + 2)

print()
print("New Hash Set: ")
hset.debug()
