#https://dmoj.ca/problem/ccc04s2
#CCC '04 S2 - TopYodeller

n,k =map(int,input().split())
scores = dict.fromkeys(range(n))

def ranks():
    r = {key: rank for rank, key in enumerate(sorted(set(d[0] for d in scores.values()), reverse=True), 1)}
    r = {k: r[v[0]] for k,v in scores.items()}
    for i in range(n):
        if scores[i][1]==None:
            scores[i][1]=r[i]
        elif scores[i][1]<r[i]:
            scores[i][1]=r[i]


for round in range(k):
    s=list(map(int,input().split()))
    for i in range(n):
        if not scores[i] ==None:
            scores[i][0]=scores[i][0]+s[i]
        else:
            scores[i] = [s[i],None]
    ranks()

best = scores[max(scores, key=scores.get)][0]
for i in scores:
    if scores[i][0]==best:
        print("Yodeller {} is the TopYodeller: score {}, worst rank {}".format(i+1,scores[i][0],scores[i][1]))
