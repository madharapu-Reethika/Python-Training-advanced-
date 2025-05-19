#searching return the last k index
'''a=[2,4,3,1,4,2,3,4,5]
k=4
for i in range(len(a)-1,-1,-1):
    if a[i]==k:
        print(i)
        break
else:
    print(-1)'''
        
#method 2
'''a=[2,4,3,1,4,2,3,4,5]
k=4
f=0
for i in range(len(a)-1,-1,-1):
    if a[i]==k:
        print(i)
        f=1
        break
if f==1:
    print(-1)'''

#binary search
'''a=[2,3,5,6,7,7,8,9,10,10,10,13,15]
l=0
r=len(a)-1
x=10
while(l<=r):
    m=(l+r)//2
    if(a[m]==x):
        print('found')
        break
    elif(x<a[m]):
        r=m-1
    else:
        l=m+1
else:
    print('not found')'''

#last index of element x
'''a=[2,3,5,6,7,7,8,9,10,10,10,13,15]
l=0
r=len(a)-1
x=10
res=-1
while(l<=r):
    m=(l+r)//2
    if(a[m]==x):
        res=m
        l=m+1 # keep going right to find the last occurrence        
    elif(x<a[m]):
        r=m-1
    elif(x>a[m]):
        l=m+1
if res!=-1:
    print(res)
else:
    print('not found')'''
    
#a[2,4,6,7,8,10,13,15] x=3 x is not in list .so place it in place to make ascending order
a=[2,4,6,7,8,10,13,15]
x=3
l=0
r=len(a)-1
pos=len(a) #default default to insert at end (if x is bigger than all elements)
while l<=r:
    m=(l+r)//2
    if a[m]<x:
        l=m+1
    else:
        pos=m
        r=m-1
a.insert(pos,x)
print(a) #leetcode 34 35
    
    