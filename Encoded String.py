def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())


stringList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
for _ in range(Ii()):
    n =  Ii()
    st = Si()
    final = ''
    for i in range(0,n-3,4):
        final += stringList[int(st[i:i+4],2)]
    print(final)