#https://dmoj.ca/problem/ccc02s2
#CCC '02 S2 - Fraction Action

import math

def simplify(x, y):
    d = math.gcd(x, y)
    x = x // d
    y = y // d
    return("{}/{}".format(x,y))

dividend = int(input())
divisor = int(input())

if (dividend//divisor == 0):
    print(simplify(dividend%divisor, divisor))
elif(dividend%divisor != 0):
    print(dividend//divisor, simplify(dividend%divisor, divisor))
else:
    print(dividend//divisor)
