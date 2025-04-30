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
stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

stack.reverse()
for i in stack._values:
    print(i)
