"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-05-24"
-------------------------------------------------------
"""
# Import
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = ["Top", "Middle", "Bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)
