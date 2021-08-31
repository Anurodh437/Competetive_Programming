def findSplitPoint(arr, n) : 
    leftSum = 0  
    for i in range(0, n) :  
        leftSum += arr[i]   
        rightSum = 0 
        for j in range(i+1, n) : 
            rightSum += arr[j]  
        if (leftSum == rightSum) : 
            return i+1 
    return -1
   
def printTwoParts(arr, n) : 
   
    splitPo = findSplitPoint(arr, n) 
    
    if (splitPo == -1 or splitPo == n ) : 
        print ("NO") 
        return
       
    for i in range(0, n) : 
        if(splitPo == i) : 
            print ("YES") 
        #print (str(arr[i]) + ' ',end='') 
   
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split())) 
    printTwoParts(arr, n)  


for _ in range(int(input())):
    x = int(input())
    arr = list(map(int, input().split()))
    if arr.count(1)%2==0 and arr.count(2)%2==0:
        print("YES")
    elif arr.count(1)%2==0 and arr.count(1)>1:
        print("YES")
    else:
        print("NO")