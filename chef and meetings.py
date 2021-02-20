def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

def timeformat24(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM": 
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:-2]

for _ in range(Ii()):
    p = Si()
    n = Ii()
    st2 = ""
    for i in range(n):
        st = Si()
        st1 = timeformat24(p).replace(":","")
        li = timeformat24(st[0:len(st)//2]).strip().replace(":","")
        ri = timeformat24(st[len(st)//2:]).strip().replace(":","")
        # print(li,len(st))
        # print(ri,st1)
        if int(li)<=int(st1)<=int(ri):
            st2 += "1"
        else:
            st2 += "0"
    print(st2)
    #print(timeformat24(st))