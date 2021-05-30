def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())

t = Ii()
for i in range(t):
    lst = Lsi()
    result = 0
    for i in range(1,int(lst[0]) + 1):
        if ord(lst[i][0]) < 91:
            x,y = 78,91
        else:
            x,y = 97,110
        if not(all(ord(j) in range(x,y) for j in lst[i])):
            result = 1
            break
    if result == 0:
        print("YES")
    else:
        print("NO")
