def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    w1,w2,x1,x2,M = Mi()
    a = x1*M
    b = x2*M
    if a <= abs(w1-w2) <= b:
        print(1)
    else:
        print(0)
