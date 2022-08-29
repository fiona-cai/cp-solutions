#https://dmoj.ca/problem/ccc96s1
#CCC '96 S1 - Deficient, Perfect, and Abundant

def dpa(n:int):
    divsum = 0
    for i in range(1,n):
        if n%i == 0:
            divsum += i

    if n>divsum:
        return f"{n} is a deficient number."
    elif n == divsum:
        return f"{n} is a perfect number."
    else:
        return f"{n} is an abundant number."

for i in range(int(input())):
    print(dpa(int(input())))
