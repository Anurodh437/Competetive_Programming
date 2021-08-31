def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

import math
t = Ii()
for _ in range(t):
    n = Ii()
    s = math.log2(n)
    if s == int(s):
        print("NO")
    else:
        print("YES")