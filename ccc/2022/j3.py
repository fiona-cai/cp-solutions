#https://dmoj.ca/problem/ccc22j3
#CCC '22 J3 - Harp Tuning

instr=input()
for i in range(len(instr)):
    if instr[i].isalpha():
        print(instr[i],end="")
    elif instr[i]=="+":
        print(" tighten", end=" ")
    elif instr[i]=="-":
        print(" loosen", end=" ")
    else:
        try:
            if instr[i].isdigit() and instr[i+1].isdigit():
                print(instr[i],end="")
            else:
                print(instr[i])
        except Exception:
            print(instr[i])
