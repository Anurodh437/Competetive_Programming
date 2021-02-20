from collections import Counter

def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

for _ in range(Ii()):
    px,py = Mi()
    s = Si() 
    # u = y+1
    # d = y-1
    # r = x+1
    # l = x-1
    a,b,c,d =0,0,0,0
    s1 = Counter(s)
    for key in s1:
        if key == "U":
            a = s1[key]
        elif key == "D":
            b = s1[key]
        elif key == "R":
            c = s1[key]
        else:
            d = s1[key]
    #print(a,b,c,d,end="   ")
    # print(x)
    # print(y)
    # if x <= px and y <= py:
    #     print("YES")
    # else:
    #     print("NO") 
    if px == 0 and py > 0:
        if a >= py:
            print("YES")
        else:
            print("NO")
    elif px == 0 and py < 0:
        if b >= py*(-1):
            print("YES")
        else:
            print("NO")
    elif py == 0 and px < 0:
        if px*(-1) <= d:
            print("YES")
        else:
            print("NO")
    elif py == 0 and px > 0:
        if px <= c:
            print("YES")
        else:
            print("NO")
        
    elif px < 0 and py < 0:
        if px*(-1) <= d and py*(-1) <= b:
            print("YES")
        else:
            print("NO")
    elif px > 0 and py < 0:
        if px <= c and py*(-1) <= b:
            print("YES")
        else:
            print("NO")
    elif px < 0 and py > 0:
        if px*(-1) <= d and py <= a:
            print("YES")
        else:
            print("NO")
    else:
        if px <= c and py <= a:
            print("YES")
        else:
            print("NO")