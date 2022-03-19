#CCC '12 J4 - Big Bang Secrets
#https://dmoj.ca/problem/ccc12j4

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

k = int(input())

s = input()
new_s = ""
cnt = 0


for letter in s:
    cnt += 1
    shift_value = (3*cnt) + k
    c_index = (alphabet.find(letter) + 1) - shift_value
    if c_index < 1:
        c_index += 26
    
    new_letter = alphabet[c_index - 1]
    new_s += new_letter

print(new_s)
