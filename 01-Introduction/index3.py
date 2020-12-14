# Python 3 version of index.py

import math

# INPUT AND OUTPUT
# Input -> 10 20 monkey
a, b, c = input().split(' ')
print(a, b, c)

# Input with map -> 10 20
a, b = map(int, input().split(' '))
print(a, b)

# Input with map -> 10, 20
a, b = map(int, input().split(','))
print(a, b)

# WORKING WITH NUMBERS
# Python has dynamic data type so integers, float are same as variables

# MATHEMATICS
# Sum Formulas -> 1 + 2 + 3 ... n = n(n+1)/2
# Sum Formulas -> 1^k + 2^k + 3^k ... n^k = n(n+1)(2n+1)/6
# Arithmetic Progression -> a + .. + b = n(a+b)/2
# Geometric Progression -> a + ak + ak^2 + .. + b = (bk -a) / (k - 1)

ap = [3, 7, 11, 15]
n = len(ap)
a = ap[1]
b = ap[-1]
print(n*(a+b)/2)

gp = [3, 6, 12, 24]
a = gp[1]
b = gp[-1]
k = 2
print((b*k - a) / (k - 1))

# Set Theory
x = set([2, 4, 7])
a = set([1, 2, 5])
b = set([2, 4])
print(x)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))

# Logic 
# Using the keywords: and, or, not
print(True and False)
print(True or False)
print(not False)

# Functions
print(3/2)
print(min([1, 2, 3]))
print(max([1, 2, 3]))
print(math.factorial(10))

# Not memoized
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(10))

# Logarithms
# logk(a, b) = logk(a) + logk(b)
# logk(x^n) = n * logk(x)
# logk(a/b) = logk(a) - logk(b)
# logu(x) = logk(x) / logk(u)
print(math.log(32, 2))
