#https://dmoj.ca/problem/ccc08j1
#CCC '08 J1 - Body Mass Index

a = float(input())
b = float(input())

bmi = a / (b * b)

if bmi > 25:
    print("Overweight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Normal weight")
