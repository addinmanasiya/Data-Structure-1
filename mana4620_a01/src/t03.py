"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-05-18"
-------------------------------------------------------
"""
# Import
from functions import file_analyze

fv = open("test.txt", "r", encoding="utf-8")
# Call
u, l, d, w, r = file_analyze(fv)
# Print
print(f"{u}, {l}, {d}, {w}, {r}")
