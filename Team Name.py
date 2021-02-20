def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n = Ii()
    lst = list(input().split())
    lst.sort()
    for i in range(n):
        for j in range(i+1,n):
            ele1 = lst[i]
            ele2 = lst[j]
            ele1[0],ele2[0] = ele2[0],ele1[0]
    print(lst)