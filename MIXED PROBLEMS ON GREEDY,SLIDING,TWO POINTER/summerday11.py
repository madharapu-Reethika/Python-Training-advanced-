#start time and end time of a meeting maximum meetings possible
# maximum non-overlapping 
#ip1=[0,3,8,1,5,7,9]
#ip2=[5,6,10,2,6,9,11]
'''def meet(s,e):
    m=sorted(zip(s,e),key=lambda x:(x[1],x[0]))
    c=0
    l=-1
    for s,e in m:
        if s>l:
            c+=1
            l=e
    return c
s=[0,3,8,1,5,7,9]
e=[5,6,10,2,6,9,11]
print(meet(s,e))'''

#reverse the string without changing the position of vowels #simtopopapuh
'''str='hippopotamus' 
vow='aeiouAEIOU'
l1=[]
for i in str:
    if i not in vow:
        l1.append(i)
l1=l1[::-1]
print(*l1)
result=''
j=0
for i in str:
    if i not in vow:
        result+=l1[j]
        j+=1
    else:
        result+=i
print(result)'''

#or
#using two pointer approach
'''s='hippopotamus'
vowels ='aeiouAEIOU'
s=list(s)
i,j=0,len(s)-1
while i<j:
    if s[i] in vowels:
        i+=1
    elif s[j] in vowels:
        j-= 1
    else:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
result = ''.join(s)
print(result)'''

#discounts=[2,1,6,4,2,3,1,1,4,1,6,7,3] take continuous elements to get max discounts
'''a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
start=0
sum1=sum(a[:k])
max=sum1
for i in range(k,len(a)):
    sum1=sum1-a[i-k]+a[i]
    if sum1>max:
        max=sum1
        start=i-k+1
print(max)
print(a[start:start+k])'''
        
#print len of longest sub array whose sum<=k
# stop when r crosess l and r goes out of index
'''a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=7
sum=0
length=0
l=0
r=0
while r<len(a): 
    sum+=a[r]
    while sum>k and l<=r:
        sum-=a[l]
        l+=1
    if sum<=k:
        length=max(length,r-l+1)
    r+=1
print(length)'''    

#or
'''a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=7
l=0
sum=0
m=0
for r in range(len(a)):
    sum=sum+a[r]
    if sum<=k:
        m=max(m,r-l+1)
    else:
        sum=sum-a[l]
        l=l+1
print(m)'''

#find the length of longest palindromic substring
#worst case
'''a='ababba'
m=0
st=0
c=0
for i in range(len(a)):
    l=i
    r=i
    while(l>=0 and r<len(a) and a[l]==a[r]): #odd length
        if (r-l+1>m):
            m=(r-l+1)
            st=l
        c+=1    
        l=l-1
        r=r+1       
    l=i
    r=i+1
    while(l>=0 and r<len(a) and a[l]==a[r]): #even length
        if(r-l+1>m):
            m=(r-l+1)
            st=l
        c+=1    
        l=l-1
        r=r+1
print(m)
print(a[st:st+m])
print(c)'''

#abcdaecdb length of longest substring without repeating char
a='abcdaecdb'
c=0
for i in range(len(a)-1):
    l=i
    r=i
    while(l>=0 and r<len(a)):
        if(a[l]!=a[r]):
            r+=1
            c+=1
        else:
            l+=1
print(c)            
        
    

        
    
    
    
    
        


    
    
    
    



    


        
        
    



    
