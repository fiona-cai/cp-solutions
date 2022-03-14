#https://dmoj.ca/problem/ccc22j2
#CCC '22 J2 - Fergusonball Ratings

n=int(input())
gold=True
golds=0
for i in range(n):
    p=int(input())
    f=int(input())
    if (p*5-f*3)>40:
        golds+=1
    else:
        gold=False

print(golds, end="")
if gold:
    print("+")
