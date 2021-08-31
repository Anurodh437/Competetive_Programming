def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())


for _ in range (int(input())):
    x = '989'
    n = Ii()
    while len(x) <= n:
        x = x+"0123456789"
    print(x[:n])
