#https://dmoj.ca/problem/ccc16j2
#CCC '16 J2 - Magic Squares

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
r4 = list(map(int, input().split()))

sum = r1[0]+r1[1]+r1[2]+r1[3]

if sum == r1[0]+r2[0]+r3[0]+r4[0]:
    if sum == r1[1]+r2[1]+r3[1]+r4[1]:
        if sum == r1[2]+r2[2]+r3[2]+r4[2]:
            if sum == r1[3]+r2[3]+r3[3]+r4[3]:
                if sum == r2[0]+r2[1]+r2[2]+r2[3]:
                    if sum == r3[0]+r3[1]+r3[2]+r3[3]:
                        if sum == r4[0]+r4[1]+r4[2]+r4[3]:
                            print("magic")
                        else:
                            print("not magic")
                    else:
                        print("not magic")
                else:
                    print("not magic")
            else:
                print("not magic")
        else:
            print("not magic")
    else:
        print("not magic")
else:
    print("not magic")
