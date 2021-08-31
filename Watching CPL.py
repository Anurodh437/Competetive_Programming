def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n,k = Mi()
    h = Li()
    h1 = []
    h2 = []
    if sum(h) < 2*k:
        print(-1)
    elif sum(h) == 2*k:
        print(len(h))
    else:
        h.sort(reverse=True)
        for i in range(len(h)):
            if i%2==0 and flag = True:
                h1.append(h[i])
                if sum(h1) > k:
                    flag = False
            else:
                h2.append(h[i])
        print(h1)
        print(h2)
