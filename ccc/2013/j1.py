#https://dmoj.ca/problem/ccc13j1
#CCC '13 J1 - Next in line

young = int(input())
middle = int(input())

diff = middle - young
old = middle + diff

print(old)
