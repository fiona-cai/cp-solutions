#https://dmoj.ca/problem/ccc15j2
#CCC '15 J2 - Happy or Sad

n = input()

x = n.count(":-)")
y = n.count(":-(")

if x == 0 and y == 0:
    print("none")
elif x == y:
    print("unsure")
elif x > y:
    print("happy")
elif x < y:
    print("sad")
