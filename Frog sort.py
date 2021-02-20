def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

import math
for _ in range(Ii()):
    n = Ii()
    w = Li()
    l = Li()
    mapdict = {}
    count = 0
    for i in range(1,n+1):
        mapdict[i] = w.index(i)
    #print(mapdict)
    for j in range(2,n+1):
        temp = 0
        if mapdict[j] <= mapdict[j-1]:
            temp = (math.ceil((mapdict[j-1]+1-mapdict[j])/l[mapdict[j]]))
        count += temp
        mapdict[j] += temp*(l[mapdict[j]])
    print(count)

