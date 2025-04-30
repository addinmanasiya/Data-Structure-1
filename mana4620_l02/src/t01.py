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

stack = Stack()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")

stack.push(1)

value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("Bottom")

stack.push("Top")

print(stack.peek())
