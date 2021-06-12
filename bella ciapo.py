def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())

for _ in  range(Ii()):
    D,d,P,Q = Mi()
    count = 0
    a = D//d
    if a%2==0:
        count+= d*((a//2)*(2*P+(a-1)*Q))
    else:
        count+= d*(a*(P+((a-1)//2)*Q))
    count+=(D%d)*(P+(a)*Q)
    print(count)