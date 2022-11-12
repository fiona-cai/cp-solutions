#https://dmoj.ca/problem/ccc11s2
#CCC '11 S2 - Multiple Choice

n = int(input())

answers = []

for i in range(n):
    answers.append(input())

cnt = 0
for i in range(n):
    correct = input()
    answer = answers[i]
    if correct == answer:
        cnt += 1
    
print(cnt)