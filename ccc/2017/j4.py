#https://dmoj.ca/problem/ccc17j4
#CCC '17 J4 - Favourite Times

d=int(input())
time=[12,0]
c=0
def add_minute(time):
    if time[1] <59:
        time[1] +=1
    else:
        time[1]=0
        if time[0]==12:
            time[0]=1
        else:
            time[0]+=1
    return time

def check_arith(time):
    diff=int(str(time[1]).zfill(2)[0])-int(str(time[1]).zfill(2)[1])
    if time[0]<10:
        if diff==time[0]-int(str(time[1]).zfill(2)[0]):
            return True
    else:
        if diff==int(str(time[0]).zfill(2)[0])-int(str(time[0]).zfill(2)[1]) and diff==int(str(time[0]).zfill(2)[1])-int(str(time[1]).zfill(2)[0]):
            return True
    return False


c=(d//720)*31
for i in range(d%720):
    if check_arith(add_minute(time)):
        c+=1

print(c)
