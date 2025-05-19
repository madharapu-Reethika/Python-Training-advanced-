# merge two different sort lists into single list
#ip:[2,4,5,8,9]
#ip:[3,5,6,9,11,12,13]
#method 1 #O(n+m)
'''
l1=[2,4,5,8,9]
l2=[3,5,6,9,11,12,13]
i=0
j=0
a=[]
for _ in range(len(l1) + len(l2)):
    if i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            a.append(l1[i])
            i += 1
        else:
            a.append(l2[j])
            j += 1
    elif i >= len(l1) and j < len(l2):
        a.append(l2[j])
        j += 1
    elif j >= len(l2) and i < len(l1):
        a.append(l1[i])
        i += 1

print(a)'''

#method 2 #O(n+m)
'''n=[2,4,5,8,9]
m=[3,5,6,9,11,12,13]
l=[]
i=j=0
while i<len(n) and j<len(m):
    if n[i]<m[j]:
        l.append(n[i])
        i+=1
    else:
        l.append(m[j])
        j+=1
l.extend(n[i:])
l.extend(m[j:])
print(l)'''

#method 3 #O(n+m)
'''a=[2,4,5,8,9]
b=[3,5,6,9,11,12,13]
c=[]
i=j=0
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
while(j<len(b)):
    c.append(b[j])
    j=j+1
while(i<len(a)):
    c.append(a[i])
    i=i+1
print(c)'''

#merge sort take an unsorted list and peform  
'''arr = [2, 4, 5, 8, 9, 3, 5, 6, 9, 11, 12, 13]
def mergesort(arr):
    if len(arr)<=1:
        return arr
    m=len(arr)//2
    l=mergesort(arr[:m])
    r=mergesort(arr[m:])
    return merge(l,r)
def merge(l,r):
    c=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            c.append(l[i])
            i+=1
        else:
            c.append(r[j])
            j+=1
    while i<len(l):
        c.append(l[i])
        i+=1
    while j<len(r):
        c.append(r[j])
        j+=1            
    return c
s=mergesort(arr)
print(s)'''

#kth highest value duplicates are not considered
#ip:[2,13,4,2,9,9,5,8,7,13,3]
#k=3 find the k highest value 3 highest value is 8 although two 9 were there
'''a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
n=max(a)
b=[]
for i in range(n+1):
    b.append(0)
for i in a:
    b[i]=1
for i in range(len(b)-1,-1,-1):
    if b[i]==1:
        k-=1
    if k<=0:
        print(i)
        break'''

#with duplicates -->13,13,9,9,...--->3rd largest becomes 9
'''a=[2,13,4,2,9,9,5,8,7,13,3]
k=3
n=max(a)
b=[]
for i in range(n+1):
    b.append(0)
for i in a:
    b[i]+=1
c=0
for i in range(len(b)-1,-1,-1):
    if b[i]<k:
        k-=b[i]
    else:
        print(i)
        break'''

#highest frequency element
'''a=[3,6,4,5,3,4,2,3]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=0
for i in d:
    if d[i]>m:
        m=d[i]
        res=i
print(m)'''

# kth highest largest element
'''a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
d={}
k=3
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=max(d.values())
b=[0 for i in range(m+1)]
for i in d:
    b[d[i]]=i
print(b[-k])'''

#find the no freq is (n/2) ip=[2,1,1,2,3,1,1] length is 7, half of 7 is 3.5
#find no which has frequency more than 3.5
#method1
'''a=[2,1,1,2,3,1,1]
n=len(a)
x=n/2
for i in range(n):
    c=0
    for j in a:
        if i==j:
            c+=1
    if c>x:
        print(i)
break'''
#method 2
'''a=[2,1,1,2,3,1,1]
d={}
for i in a:
    d[i]=d.get(i,0)+1
print(d)    
for i in d:
    if d[i]>len(a)/2:
        res=i
print(res)'''

#moyer voter problem
'''a=[2,1,1,2,3,1,1]
c=1
res=a[0]
for i in range(1,len(a)):
    if (res==a[i]):
        c=c+1
    else:
        c=c-1
        if c==0:
            res=a[i]
            c=1
print(res)'''

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
    
    

     



        
    
        
    


    


    
    