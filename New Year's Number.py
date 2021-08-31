def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n = Ii()
    a = n//2020
    a1 = a*2020
    a2 = a*2021
    if n>=a1 and n<=a2:
        print("YES")
    else:
        print("NO")