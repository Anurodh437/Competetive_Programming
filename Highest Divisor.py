def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

lst = []
N = Ii()
for _ in range(1,11):
    if N%_ == 0:
        lst.append(_)
    else:
        pass
print(max(lst))