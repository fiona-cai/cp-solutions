m = int(input())
n = int(input())

board = [["B"]*n]*m

k = int(input())
gcnt = 0
previous = {}
rcnt = 0
ccnt = 0

for choice in range(k):
    choice, number = input().split()
    if (choice, number) not in previous:
        previous[(choice, number)] = 0

        if choice == "R":
            rcnt += 1
            gcnt += n
        
        else:
            gcnt += m
            ccnt += 1


    else:
        if choice == "R":
            rcnt -= 1
            gcnt -= n
        else:
            ccnt -= 1
            gcnt -= m
        
        previous.pop((choice, number))

if rcnt != 0 and ccnt != 0: 
    overlap = rcnt*ccnt

    gcnt -= 2*(overlap)

print(gcnt)
