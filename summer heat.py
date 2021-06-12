def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    a,b,x,y = Mi()
    print(x//a + y//b)