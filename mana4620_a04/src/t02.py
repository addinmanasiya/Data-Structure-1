"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-06-09"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
from functions import queue_split_alt

source = Queue(3)

source.insert(1)

source.insert(2)

source.insert(3)

target1, target2 = queue_split_alt(source)


print("Printing Target 1...")
while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")
while len(target2) > 0:
    print(target2.remove())
