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
from functions import is_mirror_stack

string = "abcmcba"
valid_chars = "abc"

m = "m"

value = is_mirror_stack(string, valid_chars, m)

print(value)
