def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n,k = Mi()
    lst = Li()
    c = math.ceil(n/2)
    count = 0
    add1 = 0
    add = 0
    for i in lst:
        if i != -1:
            count+=1
    for i in lst:
        if i > k:
            add += 1
    for i in lst:
        if 0 <= i <= 1:
            add1 += 1
    if count < c:
        print("Rejected")
    elif add > 0:
        print("Too Slow")
    elif add1 == n:
        print("Bot")
    else:
        print("Accepted")