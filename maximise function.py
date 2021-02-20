def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n = Ii()
    lst = Li()
    res1 = 0
    res2 = 0
    lst.sort()
    res1 = res1 + abs(lst[0]-lst[1]) +abs(lst[1]-lst[-1]) + abs(lst[-1]-lst[0])
    res2 = res2 + abs(lst[0]-lst[-2]) + abs(lst[-2]-lst[-1]) + abs(lst[-1]-lst[0])
    print(max(res1,res2))