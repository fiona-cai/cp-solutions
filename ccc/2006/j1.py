#https://dmoj.ca/problem/ccc06j1
#CCC '06 J1 - Canadian Calorie Counting

a = int(input())
b = int(input())
c = int(input())
d = int(input())

cal = 0

if a == 1:
    cal += 461
elif a == 2:
    cal += 431
elif a == 3:
    cal += 420

if b == 1:
    cal += 100
elif b == 2:
    cal += 57
elif b == 3:
    cal += 70

if c == 1:
    cal += 130
elif c == 2:
    cal += 160
elif c == 3:
    cal += 118

if d == 1:
    cal += 167
elif d == 2:
    cal += 266
elif d == 3:
    cal += 75

print("Your total Calorie count is {}.".format(cal))
