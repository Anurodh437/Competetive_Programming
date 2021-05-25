def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def primecheck(a):
    primes = [n for n in range(2,a+1) if prime(n)]
    return len(primes)
# def primecheck(n):
#     prime_list = []
#     lst1 =[]
#     for i in range(2,n+1):
#         if i not in prime_list:
#             lst1.append(i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)
#     return len(lst1)


#Driver Code
for _ in range(Ii()):
    x,y = Mi()
    if primecheck(x) <= y:
        print("Chef")
    else:
        print("Divyam")


