#https://dmoj.ca/problem/ics4p1
#Word Scrambler

import itertools

s=sorted(input())
for i in itertools.permutations(s,len(s)):
    print(*i,sep="")
