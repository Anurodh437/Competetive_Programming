def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n,m = Mi()
    lst1 = Li()
    lst2 = Li()
    count = 0
    result = True

    while sum(lst1) <= sum(lst2):
        lst1.sort()
        lst2.sort()
        if lst1[0] < lst2[-1]:
            lst1[0],lst2[-1] = lst2[-1],lst1[0]
            count += 1
        else:
            result = False
            print(-1)
            break

    if result == True:
        print(count)
