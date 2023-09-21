#functions

#In-built functions
# int() str() float() min() range() max()

#Module functions
import math
print(dir(math))

import randomxs
print(dir(random))

import string
print(dir(string))

from math import sqrt
print(sqrt(4))

print("--------------------")

#User-defined functions
def sum(a, b=4):
   print(a + b)
sum(1, 2)
sum(1)
