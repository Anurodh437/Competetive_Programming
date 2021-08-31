def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

test = Ii()
for _ in range(test):
    n , k , d = Mi()
    lst = Li()
    final = sum(lst)

    if final < k:
        print(0)
    else:
        print(min(d,final//k))