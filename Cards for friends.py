def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    count = 0
    w,h,n = Mi()
    if n == 1:
        print("YES")
    elif w%2!=0 and h%2!=0:
        print("NO")
    elif w%2==0:
        while w%2!=0:
            w = w//2
            count += 2
    elif h%2==0:
        while h%2!=0:
            h = h//2
            count += 2
    else:
        print('Wrong')


def solve():
    for _ in range(geta()):
        w,h,n=geti()
        count=1
        while w%2==0:
            w//=2
            count*=2
        while h%2==0:
            h//=2
            count*=2
 
        if count>=n:
            print("YES")
        else:
            print("NO")
 
if __name__=='__main__':
    solve()