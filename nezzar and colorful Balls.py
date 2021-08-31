def Si(): return input()
def Ii(): return int(input())
def Li(): return list(map(int, input().split()))
def Mi(): return map(int, input().split())

from collections import Counter
for _ in range(Ii()):
    n = Ii()
    lst = Li()
    occurence = Counter(lst)
    print(occurence.most_common(1)[0][1])