def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n,d = Mi()
    lst = Li()
    for p in lst:
        res = False
        if p >= d*10:
            res = True
        while res!=True:
            if p%10 == d or p == 0:
                res = True
            else:
                p = p-d
            if p<0:
                break
        if res == True:
            print("YES")
        else:
            print("NO")
    