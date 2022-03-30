#https://dmoj.ca/problem/ccc00s4
#CCC '00 S4 - Golf

distance = int(input())
clubs = []
least = [5281]*(distance+1)
least[0] = 0

for x in range(int(input())):
    clubs.append(int(input()))

#every combo
for i in range(distance+1):
  for j in range(len(clubs)):
    if i + clubs[j] <= distance:
      if least[i] + 1 < least[i+clubs[j]]:
        least[i+clubs[j]] = least[i] + 1
  
if least[distance] < 5281:
  print("Roberta wins in " + str(least[distance]) + " strokes.")
else:
  print("Roberta acknowledges defeat.")
