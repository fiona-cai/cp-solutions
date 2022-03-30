#https://dmoj.ca/problem/ccc08s1
#CCC '08 S1 - It's Cold Here!

cities = []
temps = []
low = 201
a = 0
while True:
  city, temp = input().split()
  cities.append(city)
  temps.append(int(temp))
  if city == 'Waterloo':
    break
  
for i in range(len(temps)):
  if temps[i] < low:
    low = temps[i]
    a = i
    
print(cities[a])
