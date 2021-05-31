def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())

t = Ii()
for i in range(t):
    lst = Li()
    x = abs(lst[0] - lst[2]) + abs(lst[1] - lst[3])
    if x > lst[4]:
        print("NO")
    elif x == lst[4]:
        print("YES")
    elif (lst[4]-x)%2==0:
        print("YES")
    else:
        print("NO")
