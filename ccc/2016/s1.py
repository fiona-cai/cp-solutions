#https://dmoj.ca/problem/ccc16s1
#CCC '16 S1 - Ragaman

s1 = input()
l1 = len(s1)

s2 = input()
l2 = len(s2)
if (l1 == l2):    
    f = True
    for letter in s2:
        if s2.count(letter) > s1.count(letter) and letter != "*":
            print("N")
            f = False
            break
    if f == True:
        print("A")
else:
    print("N")
