#https://dmoj.ca/problem/dmopc17c5p1
#DMOPC '17 Contest 5 P1 - IOI 101

string=input()

for c in string:
  if c=="0":
    print("O", end="")
  elif c=="1":
    print("l", end="")
  elif c=="3":
    print("E", end="")
  elif c=="4":
    print("A", end="")
  elif c=="5":
    print("S", end="")
  elif c=="6":
    print("G", end="")
  elif c=="8":
    print("B", end="")
  elif c=="9":
    print("g", end="")
  else:
    print(c, end="")

print()
