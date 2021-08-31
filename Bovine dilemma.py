def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    s = set()
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            s.add(lst[j]-lst[i])
    print(len(s))
    