def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

def primecheck(a):
    if(n==2):
        return True
        exit()
    if(n%2==0):
        return False
        exit()
    for i in range(3,int(n**(1/2))+1,2):
        if(n%i==0):
            return False
            break
    else:
        return False
       