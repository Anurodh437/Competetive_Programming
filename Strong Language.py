def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())


for _ in range(Ii()):
    res = 0
    count = 0

    n,k = Mi()
    st = Si()
    if '*'not in st:
        print("NO")
    else:
        for i in range(n):
            if st[i] == '*':
                res += 1
                if res == k:
                    print("YES")
                    count += 1
                    break
            else:
                res = 0
        if count==0:
            print("NO")
