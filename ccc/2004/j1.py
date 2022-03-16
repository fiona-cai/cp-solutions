#https://dmoj.ca/problem/ccc04j1
#CCC '04 J1 - Squares

import math

a = int(input())

b = math.sqrt(a)
c = math.floor(b)

print("The largest square has side length {}.".format(c))
