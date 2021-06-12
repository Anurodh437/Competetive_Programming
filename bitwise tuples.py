def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n,m = Mi()
    res = pow(2,n,1000000007)-1
    print(pow(res,m,1000000007))