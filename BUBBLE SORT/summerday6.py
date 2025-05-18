#bubble sort 
'''a=list(map(int,input().split()))
k=2
for i in range(k,len(a)-k-1):
    for j in range(i+1,len(a)-k):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
print(a)'''

# in bubble sort take k value and and from first k values and last k should not
#..swap middle elements should swap
#not to check n-1 time always
'''arr = [64, 25, 12, 22, 11]
c=0
for j in range(len(arr)-1):
    f=False
    for i in range(len(arr) - 1-j):
        c+=1
        if arr[i] > arr[i + 1]:
            f=True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if(f==False):
        break
print(arr)
print(c)'''

#k th largest element using bubble sort
'''arr = [64, 25, 12, 22, 11]
k=2
count=0
for j in range(len(arr)-1):
    f=False
    for i in range(len(arr) - 1-j):
        count+=1
        if arr[i] > arr[i + 1]:
            f=True
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if(f==False):
        break
print(arr)
c=arr[-k]
print(c)
print(count)'''

#not using arr[-k] value print kth largest value 
'''arr = [64, 25, 12, 22, 11]
k = 2
count = 0
n = len(arr)
for j in range(k):
    f = False
    for i in range(n - 1 - j):
        count += 1
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            f = True
    if not f:
        break
print(arr)
c = arr[n - k]
print(c)
print(count)'''

#using flag swap elements before k from last and after k from first
'''a=[5,4,2,1,3,7]
k=1
c=0
for i in range(k,len(a)-k-1):
    #f=False
    for j in range(i+1,len(a)-k):
        c=c+1
        if a[j]<a[i]:
            #f=True
            a[i],a[j]=a[j],a[i]
    #if f==False:
        #break
print(a)
print(c)'''

#input [c,e,a,b,f] op=[a,b,c,e,f] using bubble sort
#alphabets sorting
'''def sorting(a):
    for i in range(len(a)-1):
        flag=False
        for j in range(len(a)-i-1):
            if ord(a[j])>ord(a[j+1]):
                flag=True
                a[j],a[j+1]=a[j+1],a[j]
        if flag==False:
            break
    return a
a=['c','e','a','f']
print(sorting(a))'''

#[[2,3],[5,1],[1,4],[2,7],[1,3]] sort based on second element
#output=[[5,1],[2,3],[1,3],[1,4],[2,7]]
'''a=[[2,3],[5,1],[1,4],[2,7],[1,3]]
n=len(a)
for i in range(n-1):
    f=False
    for j in range(n-i-1):
        if a[j][1]>a[j+1][1]:
            f=True
            a[j],a[j+1]=a[j+1],a[j]
    if f==False:
        break
print(a)'''

#LLEXOGRAPHICAL
#input:['hello','car','apples','hi'] if first letter same check 2nd and swap if second also same ..
#ouput:['apples','car','hello','hi']  whatever comes first let it be
'''a=['hello','car','apples','hi']
n=len(a)
for i in range(n-1):
    f=False
    for j in range(n-i-1):
        if  a[j][0]>a[j+1][0]:
            a[j],a[j+1]=a[j+1],a[j]
            f=True
        elif a[j][0] == a[j + 1][0] and a[j][1]==a[j+1][1]:
            
            a[j],a[j+1]=a[j],a[j+1]
            flag=True
    if f==False:
        break
print(a)'''

#input:[[4,13,12],[8,10,5],[7,9,20],[14,8,3]] sort each list according to the prime numbers
#output:[[14,8,3],[8,10,5],[7,9,20],[4,13,12]]
'''def prime(x):
    for i in x:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                break
        else:
            return i
a=[[4,13,12],[8,10,5],[7,9,20],[14,8,3]]
b=[]
for i in a:
    b.append(prime(i))
for i in range(len(b)-1):
    f=0
    for j in range(len(b)-1-i):
        if(b[j]>b[j+1]):
            b[j],b[j+1]=b[j+1],b[j]
            a[j],a[j+1]=a[j+1],a[j]
            f=1
    if(f==0):
        break
print(a)'''

#ip="an apple a day keeps doctor away"
#op='a an day away apple keeps doctor"
'''def length(w):
    c=0
    for _ in range(len(w)):
        c+=1
    return c
def sorting(a,b):
    for i in range(len(b)-1):
        f=0
        for j in range(len(b)-i-1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                a[j],a[j+1]=a[j+1],a[j]
                f=1
        if f==0:
            break
    return a           
s='An apple a day keeps the doctor away'
w=s.split()
b=[]
for i in w:
    b.append(length(i))
q=sorting(w,b)
r=' '.join(q)
print(r)'''

#sort the numbers according to the frequency
#ip:[7,2,6,3,6,7,7,2,2,2]
#op:[3,6,6,7,7,7,2,2,2,2]
'''nums = [7, 2, 6, 3, 6, 7, 7, 2, 2, 2]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
n = len(nums)
for i in range(n):
    for j in range(0, n - i - 1):
        if freq[nums[j]] > freq[nums[j + 1]]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)'''

#ip:[4,5,4,7,3,2,2,3,1,5,6,8,9,2,1,1]
#sort the numbers according to the frequency of the numbers with duplicates:
'''a=[3,5,4,4,5,6,7,7,8,8,6,4,1,1,2,8,8]
d={}
for i in a:
    if (i not in d):
        d[i]=1
    else:
        d[i]+=1
n=max(d.values())
b=[]
for i in range(n+1):
    b.append([])
#print(b)
for i in d.items():
    b[i[1]].append(i[0])
c=[]
for i in range(len(b)):
    for j in b[i]:
        c.extend([j]*i)
print(c)'''

a=['apple','hi','sir','kian']
a.sort(key=len)
print(a)

a=[[3,9],[4,2],[10,1],[5,7],[3,8]]
a.sort(key=len)
print(a)

def ab(x):
    return x[1]
a=[[3,9],[4,2],[10,1],[5,7],[3,8]]
a.sort(key=ab)
print(a)


            
    
    

