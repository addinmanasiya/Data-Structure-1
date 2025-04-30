"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-07-12"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total

# Takes a Long Time to Compute

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

for value in DATA1:
    letter = Letter(value)
    bst1.insert(letter)

for value in DATA2:
    letter = Letter(value)
    bst2.insert(letter)

for value in DATA3:
    letter = Letter(value)
    bst3.insert(letter)

file = open('otoos610.txt', 'r')

do_comparisons(file, bst1)

total = comparison_total(bst1)

file.close()

print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons:  {total:,}")


file = open('otoos610.txt', 'r')

do_comparisons(file, bst2)

total = comparison_total(bst2)

file.close()

print()
print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons:  {total:,}")

file = open('otoos610.txt', 'r')

do_comparisons(file, bst3)

total = comparison_total(bst3)

file.close()

print()
print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons:  {total:,}")
