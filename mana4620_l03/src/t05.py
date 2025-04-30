"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-05-31"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = int(input("Enter a number: "))

pq.insert(value)

print(pq.remove())
