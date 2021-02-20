def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())
 
for _ in range(Ii()):
    s = Si()
    s1 = list(s)
    for i in range(len(s1)):
        if i%2==0:
            if s1[i] == "a":
                s1[i]="b"
            else:
                s1[i] = "a"
        else:
            if s1[i] == "z":
                s1[i] ="y"
            else:
                s1[i] = "z"
    print("".join(s1))   