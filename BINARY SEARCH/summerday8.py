#square root of a number
'''num=38
sqrt=int(num**0.5)
print(sqrt)'''

#square root of a number
'''def sqrt(n):
    if n==0 or n==1:
        return n
    start,end=1,n
    ans=0
    while start<=end:
        mid=(start+end)//2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans
print(sqrt(38))'''

#given an ascending order rotated array find the index of first element
#ip:[15,18,20,22,2,5,8,10,12,13]

#method 1
'''a=[15,18,20,22,2,5,8,10,12,13]
m=0
l=0
r=len(a)-1
c=0
while l<=r:
    if(a[l+1]>a[l]):
        l+=1
        c+=1
    else:
        print(l+1)
        break
print(c+1)'''

#method 2 using binary search
'''a=[15,18,20,22,2,5,8,10,12,13]
def rotate(a):
    l=0
    r=len(a)-1
    while l<r:
        m=(l+r)//2
        if a[m]>a[r]:
            l=m+1
        else:
            r=m   
    return a[r]
print(rotate(a))'''

#Find peak Element method 1w
'''def peaks(arr):
    peaks = []
    n = len(arr)   
    for i in range(1, n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peaks.append(arr[i])
    return peaks
a = [2, 3, 4, 6, 3, 2, 1, 5, 8, 10, 1, 4, 2]
print(*peaks(a))'''

#method 2
'''def peak_ele(a,l,r):
    while l<=r:
        m=(l+r)//2            
        if a[m]>a[m+1] and a[m]>a[m-1]:
            return a[m]
        else:
            l=m+1         
    return a[m]        

a=[2,3,4,6,3,2,1,5,8,10,1,4,2]
n=len(a)-1
print(peak_ele(a,0,n))'''

#method 3 which will return first element last element along with middle peaks
'''a=[5,2,4,6,7,8 ,6,5,4,6,7,8,9,10,8,6,5,4,7]
l=0
r=len(a)-1
while(l<r):
    m=(l+r)//2
    if(m==0 or a[m]>a[m+1] and m==n-1 or a[m]>a[m-1]):
        print(a[m])
        break
    if(a[m+1]>a[m]):
        l=m+1
    else:
        r=m-1'''
       
       
#give[3,6,7,11] h=8 k=3 can in 8 hours koko and banana
#yes or no
'''import math
a=[3,6,7,11]
h=8
k=6
s=0
for i in range(len(a)):
    s=s+math.ceil(a[i]/k)
if s<=h:
    print('yes')
else:
    print('no')'''

#find k 
'''import math
a=[3,6,7,11]
h=8
k=1
while(1):
    s=0
    for i in range(len(a)):
        s=s+math.ceil(a[i]/k)
        if(s>h):
            k=k+1
            break
    else:
        print(k)
        break'''

'''def pos(a,k,h):
    s=0
    for i in a:
        s=s+math.ceil(a[i]/k)
        if s<=h:
            return True
        else:
            return False
l=1
r=max(piles)
res=r
while(l<=r):
    m=(l+r)//2
    if(pos(piles,m,h)):
        res=m
        r=m-1
    else:'''

#aggressive cows problem
#linear search (n log n)
a=[1,2,5,7,10]
k=3   #no of cows
min=4 #min dist but maximum from min numbers from list
k=k-1

first=a[0]
for i in a:
    if i-first>=min:
        first=i
        k=k-1
if k<=0:
    print('yes')
else:
    print('no')


        
            
    
    
    
        



        
        

