from random import random
import sys
import os
from icecream import ic
from sympy import symbols
  
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from source.RandomFunctionGenerator import random_function, generate_random_functions

var = symbols('x')
consts = symbols('a b c d')

random_functions = set()   # set --> no duplicates
for i in range(20):
    random_functions.add(random_function([var], consts, max_depth=4))

random_functions = list(random_functions)

# for foo in random_fuctions:
#     print(foo)

random_functions = generate_random_functions([var], consts, amount=20, max_depth=4)
for foo in random_functions:
    print(foo)


