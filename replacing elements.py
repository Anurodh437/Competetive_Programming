def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n ,d = Mi()
    a = Li()
    a.sort()
    if a[-1] <= d or a[0] + a[1] <= d:
        print('YES')
    else:
        print("NO")