#https://dmoj.ca/problem/ccc13s1
#CCC '13 S1 - From 1987 to 2013

def checkDigits(n):
    prev = []
    for i in str(n):
        if i in prev:
            return False
        else:
            prev.append(i)
    
    return True



n = int(input()) + 1

while True:
    if checkDigits(n):
        print(n)
        break
    else:
        n +=1
