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
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["1", "2", "3", "4"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)
