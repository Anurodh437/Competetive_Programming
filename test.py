def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

def separate(l1,l2):
    a = len(set(l1+l2))
    return a
for _ in range(Ii()):
    n = Ii()
    st = input().split()
    dic = {}
    for i in st:
        l = i[1:]
        if l in dic:
            dic[l].append(i[0])
        else:
            dic[l] = [i[0]]
    final = list(dic.keys())
    temp = 0
    for i in range(len(dic)):
        for j in range(i+1,len(dic)):
            temp1 = separate(dic[final[i]],dic[final[j]])
            temp += (temp1-len(dic[final[i]]))*(temp1-len(dic[final[j]]))
            res = 2*temp
    print(res)