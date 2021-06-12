from typing import Dict


def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    N,M = Mi()
    a = Li()
    b = Li()
    dct = dict()
    MAX = 1e+9 

    for i in range(N):
        if i==0:
            dct[i] = 0
        elif a[i]!=0:
            dct[i] = 0
        else:
            dct[i] = MAX
    
    final1 = -1
    for i in range(N):
        if(a[i] == 1):
            final1 = i
        if final1 != -1:
            if a[i] == 0:
                dct[i] = min(dct[i],i-final1)
 
    final2 = -1
    for i in range(N-1,-1,-1):
        if(a[i] == 2):
            final2 = i
        if final2 != -1:
            if a[i] == 0:
                dct[i] = min(dct[i],final2 - i)

    for i in range(M):
        c = b[i] - 1
        if dct[c]!= MAX:
            print(dct[c],sep = " ")
        else:
            print(-1,sep = " ")