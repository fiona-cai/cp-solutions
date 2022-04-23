#https://dmoj.ca/problem/geometry1
#Troubling Triangles

import math

for _ in range(int(input())):
	x1,y1,x2,y2,x3,y3=map(int,input().split())
	area=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
	perimeter=math.sqrt(((x2-x1)**2)+(y2-y1)**2)+math.sqrt(((x3-x1)**2)+(y3-y1)**2)+math.sqrt(((x2-x3)**2)+(y2-y3)**2)
	print('{:.2f}'.format(round(area,2)),end=" ")
	print('{:.2f}'.format(round(perimeter,2)))
