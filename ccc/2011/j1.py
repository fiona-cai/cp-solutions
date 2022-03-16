#https://dmoj.ca/problem/ccc11j1
#CCC '11 J1 - Which Alien?

a = int(input())
b = int(input())

if a >= 3 and b <= 4:
    print("TroyMartian")
if a <= 6 and b >= 2:
    print("VladSaturnian")
if a <= 2 and b <= 3:
    print("GraemeMercurian")
