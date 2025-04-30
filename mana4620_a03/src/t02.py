"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-06-01"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

source1 = Stack()
source2 = Stack()
target = Stack()

source1.push(8)
source1.push(12)
source1.push(8)
source1.push(5)

source2.push(14)
source2.push(9)
source2.push(7)
source2.push(1)
source2.push(6)
source2.push(3)

target.combine(source1, source2)

for i in target:
    print(i)
