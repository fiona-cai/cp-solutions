#https://dmoj.ca/problem/ccc03s2
#CCC '03 S2 - Poetry

def lastVowel(s):
  a = 0
  for i in range(len(s)):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
      a = i
  return s[a:]

n = int(input())
for i in range(n):
  l1 = str(input().lower()).split()
  l1 = l1[-1]
  l2 = str(input().lower()).split()
  l2 = l2[-1]
  l3 = str(input().lower()).split()
  l3 = l3[-1]
  l4 = str(input().lower()).split()
  l4 = l4[-1]
  l1 = lastVowel(l1)
  l2 = lastVowel(l2)
  l3 = lastVowel(l3)
  l4 = lastVowel(l4)

  if l1 == l2 and l2 == l3 and l3 == l4:
    print("perfect")
  elif l1 == l2 and l3 == l4:
    print("even")
  elif l1 == l3 and l2 == l4:
    print("cross")
  elif l1 == l4 and l2 == l3:
    print("shell")
  else:
    print("free")
