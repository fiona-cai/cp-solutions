#CCC '12 S2 - Aromatic Numbers
#https://dmoj.ca/problem/ccc12s2

s = input()

symbolToValues = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
aprev = 0
curra = 0
rprev = 999999999
sum = 0
for i in range(len(s)):
    symbol = s[i]
    if i % 2 == 1:
        r = symbolToValues[symbol]
        if r > rprev:
            sum -= aprev*rprev
            sum -= aprev*rprev
        
        sum += curra*r
        rprev = r
        aprev = curra
    else:
        curra = int(symbol)

print(sum)
