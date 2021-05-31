def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Lsi(): return input().split()
def Mi(): return map(int, input().split())
import math

t = Ii()
for i in range(t):
    n = Ii()
    print(math.ceil(n/2))