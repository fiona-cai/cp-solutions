#https://dmoj.ca/problem/ccc14s3
#CCC '14 S3 - The Geneva Confection

import sys
input = sys.stdin.readline


t = int(input())
for __ in range(t):
    n = int(input())

    cars = []

    for _ in range(n):
        cars.append(int(input()))

    branch = []
    nextcarneeded = 1

    while True:
        if len(cars) == 0 and len(branch) != 0:
            if branch[len(branch)-1] != nextcarneeded:
                print("N")
                break 


        if len(branch) != 0:
            if branch[len(branch)-1] == nextcarneeded:
                branch.pop(len(branch)-1)
                nextcarneeded += 1
                if nextcarneeded > n:
                    print("Y")
                    break
                

        if len(cars) == 0 and len(branch) == 0:
            print("N")
            break
        if len(cars) != 0:
            if len(branch) == 0:
                if cars[len(cars)-1] == nextcarneeded:
                    cars.pop(len(cars)-1)
                    nextcarneeded += 1
                    if nextcarneeded > n:
                        print("Y")
                        break
                else:
                    topcar = cars.pop(len(cars)-1)
                    branch.append(topcar)
            elif branch[len(branch)-1] != nextcarneeded:
                if cars[len(cars)-1] == nextcarneeded:
                    cars.pop(len(cars)-1)
                    nextcarneeded += 1
                    if nextcarneeded > n:
                        print("Y")
                        break
                else:
                    topcar = cars.pop(len(cars)-1)
                    branch.append(topcar)

        else:
            if branch[len(branch)-1] != nextcarneeded:
                print("N")
                break
