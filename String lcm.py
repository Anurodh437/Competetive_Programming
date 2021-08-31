def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

# for _ in range(Ii()):
#     s = Si()
#     t = Si()
#     i = 1
#     while s != t :
#         s = s * i
#         t = t * i
#         i+=1
#         if s == t:
#             break
#             print(s)
#     else:
#         print(-1)

from math import gcd
for _ in range(Ii()):
    a = Si()
    b = Si()
    l1 = len(a)
    l2 = len(b)
    lcm = l1*l2//gcd(l1,l2)
    a*=lcm//l1
    b*=lcm//l2
    if a == b:
        print(a)
    else:
        print(-1)