#https://dmoj.ca/problem/ccc15s1
#CCC '15 S1 - Zero That Out

x = int(input())
commands = []

while x > 0:
    y = int(input())
    commands.append(y)
    if y == 0:
        commands.pop()
        commands.pop()
    x -= 1

sum = 0

for i in commands:
    sum += i

print(sum)
