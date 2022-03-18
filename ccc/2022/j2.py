#https://dmoj.ca/problem/ccc22j2
#CCC '22 J2 - Fergusonball Ratings

n=int(input())
golds=0
for i in range(n):
    a=int(input())
    b=int(input())
    rating=a*5-b*3
    if rating > 40:
        golds+=1

if golds == n:
    print("{}+".format(golds))
else:
    print(golds)
