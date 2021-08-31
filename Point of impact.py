def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    n,k,x,y = Mi()

    if x == y:
        print(n,n)

    else:
        SidesList=[]
        if x>y:
            SidesList=[[n,y+n-x],[y+n-x,n],[0,x-y],[x-y,0]]
        else:
            SidesList=[[x+n-y,n],[n,x+n-y],[y-x,0],[0,y-x]]
        ans = SidesList[(k-1)%4]
        print(ans[0],ans[1])