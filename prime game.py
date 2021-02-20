def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

from math import sqrt,ceil

# def factList(a):
#     lst =[]
#     for i in range(1,a+1):
#         lst.append(i)
#     return lst
# # print(factList(7))
# def primeCount(b):
#     count = 0
#     wrong = 0
#     for k in factList(b):
#         if k > 1:
#             for j in range(2,ceil(sqrt(k))):    
#                 if k % j == 0:
#                     wrong += 1
#                 else:
#                     count+=1
#     return count+2

# print(primeCount(5))
# for _ in range(Ii()):
#     x,y = Mi()
#     if primeCount(x) <= y:
#         print("Chef")
#     else:
#         print("Divyam")

def primecheck(n):
    lst = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(2, n+1):
        if prime[p]:
            lst.append(p)
    return lst
for _ in range(Ii()):
    x,y = Mi()
    print(primecheck(x))
    # if primecheck(x) <= y:
    #     print("Chef")
    # else:
    #     print("Divyam")