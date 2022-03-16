#https://dmoj.ca/problem/ccc09j1
#CCC '09 J1 - ISBN

a = int(input())
b = int(input())
c = int(input())

s = (9+7*3+8+0*3+9+2*3+1+4*3+1+8*3) + (a + b * 3 + c)

print("The 1-3-sum is {}".format(s))
