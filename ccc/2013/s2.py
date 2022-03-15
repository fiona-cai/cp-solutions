#https://dmoj.ca/problem/ccc13s2
#CCC '13 S2 - Bridge Transport

MAX = int(input())
TOTAL_TRAINS = int(input())
trains = [0,0,0]

for i in range(TOTAL_TRAINS):
  trains.append(int(input()))
trains.append(MAX+1)
  
done = 0
i = 3
sum = trains[i-3] + trains[i-2] + trains[i-1] + trains[i]
while sum <= MAX:
    done += 1
    i = i + 1
    sum = trains[i-3] + trains[i-2] + trains[i-1] + trains[i]
print(done)
