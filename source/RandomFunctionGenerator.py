import sympy
from sympy import symbols, srepr, series
import random
from random import sample, choice
import numpy as np


def Div(x,y):
    """Division sympy. Needed for random sampling of functions"""
    return sympy.Mul(x, sympy.Pow(y, sympy.Integer(-1)))

unary_functions = [sympy.sqrt, sympy.sin, sympy.cos, sympy.exp, sympy.tan, sympy.sinh, sympy.cosh, sympy.tanh]
binary_functions = [sympy.Mul, sympy.Pow, sympy.Add, Div]

def random_function(vars, consts, depth = 0, max_depth = 1):
    """
    Randomly generate a function that contains the variables in `vars` and constants in `consts`.
    Functions are chained up to `max_depth`, but might also be shorter
    """
    if depth >= max_depth:
        # at max depth only var or const
        next_step = np.random.choice(["var", "const"], p=[0.9,0.1])
        if next_step == "var":
            return choice(vars) 
        else:
            return choice(consts)

    if depth > 0:
        next_step = np.random.choice(["var", "const", "func"], p=[0.1, 0.1, 0.8])

        if next_step == "var":
            return choice(vars)
        if next_step == "const":
            return choice(consts)

    next_step = np.random.choice(["unary_func", "binary_func"], p=[0.5, 0.5])
    
    if next_step == "unary_func":
        return choice(unary_functions)(random_function(vars, consts, depth = depth+1, max_depth=max_depth))
    elif next_step == "binary_func":
        return choice(binary_functions)(
            random_function(vars, consts, depth = depth+1, max_depth=max_depth),
            random_function(vars, consts, depth = depth+1, max_depth=max_depth)
            )

    return sympy.simplify(rnd_func)

def generate_random_functions(vars, consts, amount=1, max_depth=4):
    random_functions = set()   # set --> no duplicates
    for i in range(amount):
        random_functions.add(random_function(vars, consts, max_depth=max_depth))
    return list(random_functions)