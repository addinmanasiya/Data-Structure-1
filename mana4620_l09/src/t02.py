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

hset = Hash_Set(20)

hset.insert(100)

hset.insert(200)

hset.insert(300)

print("Printing hset: ")
for value in hset:
    print(value)

removed = hset.remove(200)

print()
print("Removed Value: ")
print(removed)

print()
print("Printing hset: ")
for value in hset:
    print(value)
