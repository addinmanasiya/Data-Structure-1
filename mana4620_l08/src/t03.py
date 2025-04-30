"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-07-05"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import DATA1, fill_letter_bst


bst = BST()

fill_letter_bst(bst, DATA1)

for value in bst:
    print(value.letter, value.code)
