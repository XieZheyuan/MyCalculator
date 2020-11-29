from math import *


def square(x):
    return x ** 2


def mod(x, y):
    return x % y


def cube(x):
    return x ** 3


def subtriplicate(x):
    return x ** (1 / 3)


def csc(x):
    return 1 / sin(x)


def sec(x):
    return 1 / cos(x)


def cot(x):
    return 1 / tan(x)


def fact(x):
    return factorial(x)


def ln(x):
    return log(x, e)


def A(n, m):
    return factorial(n) / factorial(n - m)


def C(n, m):
    return A(n, m) / factorial(m)


def count(v, val_ans=0):
    v = v.replace("Val:Ans", str(val_ans))
    v = v.replace("^", "**")
    return str(eval(v))
