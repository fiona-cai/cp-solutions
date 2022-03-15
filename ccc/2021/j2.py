#https://dmoj.ca/problem/ccc21j2
#CCC '21 J2 - Silent Auction

n = int(input())

bids = []

for i in range(n):
    name = input()
    bid = int(input())

    bids.append([bid, name])

my_max = 0
output = ""

for i in bids:
    if i[0] > my_max:
        output = i[1]
        my_max = i[0]

print(output)
