def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    ans = 0
    ans1 = 0
    n = Ii()
    lst = Li()
    for i in lst:
        if i%2 != 0:
            ans = ans + 1
        else:
            ans1 = ans1 + 1
    print(min(ans,ans1))