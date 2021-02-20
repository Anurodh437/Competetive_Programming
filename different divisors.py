def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

def num_factors(x):
        lst = []
        for i in range(1, x + 1):
            if x % i == 0:
                lst.append(i)
            return lst

d = Ii()
print(num_factors(d))
    
    

