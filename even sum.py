def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

def gapsum(l):
    c = sum(l[::2]) - sum(l[1::2])
    return c

for _ in range(Ii()):
    n = Ii()
    lst = Li()
    if gapsum(lst) % 2 == 0:
        print(1)
    else:
        print(2)