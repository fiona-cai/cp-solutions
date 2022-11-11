#https://dmoj.ca/problem/ccc10s3
#CCC '10 S3 - Firehose

import sys
input = sys.stdin.readline
def checkFirehosePlacements(place, houses, length, visited):
    housenum = -1
    firstNotVisited = -1
    found = False
    for house in houses:
        housenum += 1
        
        if place + length > 999999:
            if place - length <= house or house <= place + length - 1000000:
                visited[housenum] = True
        if place - length < 0:
            if 1000000 + (place-length) <= house or house <= place + length:
                visited[housenum] = True


        if place - length <= house <= place + length:
            visited[housenum] = True
        
        if found == False:
            if visited[housenum] == False:
                firstNotVisited = housenum
                found = True
    
    return firstNotVisited
    

def checkFirehoseLength(length, houses, k):
    orik = k
    firstNotVisited = 0
    total_visited = [False]*len(houses) 
    for house in range(len(houses)):
        if total_visited[house] == False:
            visited = [False]*len(houses) 
            housenum = -1
            k = orik
            while k > 0:
                if housenum == -1:
                    housenum += 1
                    currhouse = house
                else: currhouse = firstNotVisited
                
                place = houses[currhouse] + length

                if place > 999999:
                    place = place - 1000000

                firstNotVisited = checkFirehosePlacements(place, houses, length, visited)

                k -= 1

                work = False
                for i in range(len(visited)):
                    if visited[i] == True:
                        total_visited[i]  = True
                        work = True
                    else:
                        work = False
                        break
                
                if work:
                    return True

            
    return False
            

h = int(input())

houses = []

for _ in range(h):
    houses.append(int(input()))

houses.sort()

k = int(input())

top = 1000000
low = 0

lastworkedmid = 0

while True:
    mid = (top+low)//2

    if low > top:
        print(lastworkedmid)
        break
        

    if checkFirehoseLength(mid, houses, k):
        top = mid - 1
        lastworkedmid = mid
    else:
        low = mid +1