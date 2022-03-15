#https://dmoj.ca/problem/ccc13s1
#CCC '13 S1 - From 1987 to 2013

D = int(input())

done = 0

D += 1

while done == 0:
    c = 0
    digits = list(str(D))
    for digit in digits:
        if digits.count(digit) == 1:
            c += 1
        else:
            D += 1
            break
    if c == len(digits):
        done += 1
        print(D)
