#https://dmoj.ca/problem/ccc14j1
#CCC '14 J1 - Triangle Times

one = int(input())
two = int(input())
three = int(input())

sum = one + two + three

if sum == 180:
    if one == two and one == three:
        print("Equilateral")
    elif one == two or one == three or two == three:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
