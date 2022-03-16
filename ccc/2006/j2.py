#https://dmoj.ca/problem/ccc06j2
#CCC '06 J2 - Roll the Dice

m = int(input())
n = int(input())

correct = 0
answers = [(1,9), (2,8), (3,7), (4,6), (5,5), (6,4), (7,3), (8,2), (9,1)]

for x,y in answers:
    for a in range(1,m+1):
        for b in range(1, n+1):
            if x == a and y == b:
                correct += 1
        
sent1 = "There are"
sent2 = "There is"

ence1 = "ways"
ence2 = "way"

if correct == 1:
    sent = sent2
    ence = ence2
else:
    sent = sent1
    ence = ence1

print("{0} {1} {2} to get the sum 10.".format(sent, correct, ence))
