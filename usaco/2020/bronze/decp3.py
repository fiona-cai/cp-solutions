#https://dmoj.ca/problem/usaco20decb3
#USACO 2020 December Bronze P3 - Stuck in a Rut

n = int(input())

class inter:
	def __init__(self, x0, y0, a0, b0):
		self.x, self.y, self.a, self.b = x0, y0, a0, b0
	
lst = []
north = []
east = []
cowpos = []
for _ in range(n):
	d,x,y = input().split()
	x = int(x)
	y = int(y)
	if d == "E": east.append((x,y, _+1))
	else: north.append((x,y, _+1))
	cowpos.append([x,y])


for x,y, i in north:
	for a,b, j in east:
		if x < a or b < y: continue
		lst.append(inter(x,b,i, j))
	
lst.sort(key = lambda e : (e.x, e.y))
inf = 99999999999
cows = [inf]*(n+1)

for i in lst:
	x,y,a,b= i.x, i.y, i.a, i.b
	if cows[a] == cows[b] == inf:
		cowposa = cowpos[a-1]
		cowposb = cowpos[b-1]
		d1 = (x - cowposa[0])   + (y-cowposa[1])
		d2 = (x - cowposb[0]) +  (y - cowposb[1])
		if d1 > d2:
			cows[a] = d1
		elif d1 == d2:
			continue
		else: 
			cows[b] = d2

for i in range(1, n+1):
	if cows[i] == inf:
		print("Infinity")
	else:
		print(cows[i])
