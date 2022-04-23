#https://dmoj.ca/problem/bf1
#List Minimum

a = int(input())
b = a
el = []

while a > 0:
    el.append(int(input()))
    a -= 1

while b > 0:
    print(min(el))
    try:
        el.remove(min(el))
    except:
        break
    b -= 1
