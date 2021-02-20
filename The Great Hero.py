def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

from math import ceil,floor
for _ in range(Ii()):
    a,b,n = Mi()
    at = Li()
    flag = True
    ht = Li()
    for i in range(n):
        k = ht[i]/a
        if k == int(k):
            k = k-1
        else:
            k = floor(k)
        b = b - (k)*at[i]
        if b <= 0:
            flag =False
            break
        #print("health :  ",b) 
    if flag == False:
        print("NO")
    else:
        print("YES")
    