#https://dmoj.ca/problem/ccc05j1
#CCC '05 J1 - The Cell Sell

d = int(input())
e = int(input())
w = int(input())

A = ((d - 100) * 25 if d-100 > 0 else 0) + 15 * e + 20 * w
B = ((d - 250) * 45 if d-250 > 0 else 0) + 35 * e + 25 * w

print("Plan A costs %.2f\nPlan B costs %.2f" % (A/100, B/100))
if A < B:
    print("Plan A is cheapest.")
elif B < A:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")
