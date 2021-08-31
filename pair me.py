def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    x,y,z = Mi()
    if x + y == z:
        print("YES")
    elif y + z == x:
        print("YES")
    elif z + x == y:
        print("YES")
    else:
        print("NO") 