#Binary search aggressive cows
'''a=[1,2,5,7,10]
a.sort()
l=0
r=a[-1]-a[0]
res=0
while l<=r:
    c=3
    m=(l+r)//2
    prev=a[0]
    c-=1
    for i in range(1,len(a)):
        if a[i]-prev>=m:
            c-=1
            prev=a[i]
        if c==0:
            break
    if c<=0:
        res=m
        l=m+1
    else:
        r=m-1
print(res)'''

#searching an element in the given matrix    
#method 1  
'''a= [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
x=5
flag=False
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == x:
            flag = True
            break
    if flag:
        break

if flag:
    print("found")
else:
    print("not found")'''

#method 2
'''a= [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
x=5
flag=False
for i in a:
    if x in i:
        flag = True
        break
if flag:
    print('found')
else:
    print('not')'''

#method 2 O(n*m)
'''a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
x=23
flag=False
for i in a:
    if i[-1]>=x:
        for element in i:
            if element==x:
                found=True
            break
        break
if found:
    print('found')
else:
    print("not found")'''
    
# checking with first element of a row and last element of a row  
#a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
'''def binary(a,x):
    l=0
    r=len(arr)-1
    while(l<=r):
        m=(l+r)//2
        if(a[m]==x):
            return 1
        elif(a[m]>x):
            r=m-1
        else:
            l=m+1
    return 0
a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
x = 23
for i in a:
    f=1
    if(a[0]<=x and a[-1]>=x):
        if(binary(i,x)):
            f=0
            print('found')
            break
if(f==1):
    print('no')
else:
    print('yes')'''

#VERY OPTIMAL CODE O(n+logm)
'''a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
x=23
n=len(a)
m=len(a[0])
l=0
r=n*m-1
flag=False
while l<=r:
    mid=(l+r)//2
    row=mid//m
    col=mid%m
    if a[row][col]==x:
        flag=True
        break        
    elif a[row][col]<x:
        l=mid+1
    else:
        r=mid-1
if flag:
    print("found")
else:
    print("not found")'''

#capacity to ship packages within d days
'''a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cap=12
d=1
s=0
if cap<max(a):
    print("not")
else:
    for i in a:
        if s+i<=cap:
            s+=i
        else:
            d+=1
            s=i
    print(d)'''

#search a 2D Matrix
''''a=[[3,4,6,8],[5,7,9,40],[8,12,13,50],[20,23,26,60],[30,36,40,70]]
def searchMatrix(matrix, target):
        if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1       
    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1
        else:
            row += 1

    return False

#or
        i=0
        j=len(matrix[0])-1
        n=len(matrix)

        while(i<n and j>=0):
            if(matrix[i][j]==target):
                return True
            elif(matrix[i][j]>target):
                j-=1
            else:
                i+=1
        return False
'''    
#TWO SUM(2 pointer approach)
a=[2,7,11,15]
k=9
i=0
j=len(a)-1
while(i<j):
    if a[i]+a[j]==k:
        print(i,j)
        break
    elif(a[i]+a[j]<k):
        i+=1
    else:
        j-=1

#three sum
a=[-1,0,1,2,-1,-4]
a.sort()
for i in range(len(a)):
    l=i+1
    r=len(a)-1
    while l<r:
        s=a[i]+a[l]+a[r]
        if s==0:
            print(a[i],a[l],a[r])
            l+=1
            r-=1
        elif  s<0:
            l+=1
        else:
            r-=1

        
        
    
    
    



    
        
