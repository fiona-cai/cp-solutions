#https://dmoj.ca/problem/ccc15s2
#CCC '15 S2 - Jerseys

J = int(input())
A = int(input())
jerseys = []
sizes = []
numbers = []
count = 0
for _ in range(J):
  size = input()
  if size == "S":
    jerseys.append(0)
  elif size == "M":
    jerseys.append(1)
  else:
    jerseys.append(2)
    

for _ in range(A):
    size, number = input().split()
    if size == "S":
      sizes.append(0)
    elif size == "M":
      sizes.append(1)
    else:
      sizes.append(2)
    numbers.append(int(number))

for i in range(A):
  try:
    if jerseys[numbers[i]-1] >= sizes[i]:
      jerseys[numbers[i]-1] = -1
      count+=1
  except Exception:
    print(i)
    pass
    
print(count)
