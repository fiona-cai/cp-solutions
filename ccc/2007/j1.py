#https://dmoj.ca/problem/ccc07j1
#CCC '07 J1 - Who is in the Middle?

a = int(input())
b = int(input())
c = int(input())
list = []

list.append(a)
list.append(b)
list.append(c)
middle = sorted(list)[1]

print(middle)
