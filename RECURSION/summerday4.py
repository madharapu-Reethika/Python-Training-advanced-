#count the frequency of a number my code is functional
'''a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=6
def freq(a,k,i=0):
    if i==len(a):
        return 0 #as it is functional return 0 because c not inside
    if a[i]==k:
        return 1+freq(a,k,i+1)
    else:
        return freq(a,k,i+1)
print(freq(a,k))'''

#paramaterized means count varaible inside the function def
'''a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=3
def freq(a,k,i=0,c=0):
    if i==len(a):
        return c
    if a[i]==k:
        #c=c+1
        return freq(a,k,i+1,c+1)
    return freq(a,k,i+1,c)
print(freq(a,k))'''

#print the number when frequency of a number is given
'''def freq(a,k,i=0):
    if i==len(a):
        return 0 
    if a[i]==k:
        return 1+freq(a,k,i+1)
    else:
        return freq(a,k,i+1)
x=[2,4,6,3,3,2,6,1,2,3,6,6,5]
f=3    
def iterate(x,f,i=0):
    if(i==len(x)):
        return 'no found'
    if(freq(x,x[i])==f):
        return x[i]
    return iterate(x,f,i+1)
print(iterate(x,f))'''

#using dictionary
'''from collections import Counter
def count(ct,k,keys,l,i=0):
    if i==len(keys):
        return l
    if ct[keys[i]]==k:
        l.append(keys[i])
    return count(ct,k,keys,l,i+1,)
        
a=[2,4,6,3,3,2,6,1,2,3,6,6,5]
k=1
ct=Counter(a)
keys=list(ct.keys())
print(count(ct,k,keys,l=[]))'''

#using dictionary
'''def value(x,f,d,i=0):
    if(i==len(x)):
        return 'no'
    if(d[x[i]]==f):
        return x[i]
    return value(x,f,d,i+1)
def fre_d(x,f,d={},i=0):
    if(i==len(x)):
        return value(list(d.keys()),f,d)
    if(x[i] not in d):
        d[x[i]]=1
    else:
        d[x[i]]+=1
    return fre_d(x,f,d,i+1)
a=[2,2,3,3,4,5,4,3,3,4,5,6,7]
f=3
print(fre_d(a,f))'''

#subset [2,3,4] print all the subsets [2],[2,3],[2,4],[2,3,4],[3],[3,4],[4] using recusrion
'''def subset(x,s=[],i=0):
    if i==len(x):
        print(s)
        return 
    subset(x,s+[x[i]],i+1)
    subset(x,s,i+1)
a=[2,3,4]
subset(a)'''


#subset [2,3,4] sumofsub=k=6 find whether subsum is true or not
#not so optimized code
'''def sub(x,k,i=0):
    if k==0:
        return True
    if i==len(x):
        return False
    if x[i]>k:
        return sub(x,k,i+1)
    return sub(x,k-x[i],i+1) or sub(x,k,i+1)
a=[2,3,4]
k=6
print(sub(a,k))'''

 #print the no of lists sum is k
'''a=[1,2,4,5]
key=6
def sum_key_subset(a,key,i=0,d=[]):
    if i==len(a):
        if sum(d)==key:
            print(d)
        return
    sum_key_subset(a,key,i+1,d+[a[i]])
    sum_key_subset(a,key,i+1,d)
sum_key_subset(a,key)'''

#same code few changes
'''def sum_subset(a,k,x=[],i=0):
    if i==len(a):
        if k==0:
            print('True')
            print(x)
        return
    if a[i]<=k:
        sum_subset(a,k-a[i],x+[a[i]],i+1)
    sum_subset(a,k,x,i+1)

a=[2,3,4]
k=5
sum_subset(a,k)'''

#given list [2,4,6,8] sum=14 find min no of coins required to get sum
'''def sum_subset(a,k,x=0,i=0,m=999999):
    if i==len(a):
        if k==0:
            if(s<m):
                m=s
        return m
    if a[i]<=k:
        sum_subset(a,k-a[i],x+1,i+1)
    sum_subset(a,k,x,i+1)

a=[2,4,6,8]
k=14
m=sum_subset(a,k)
if m==999999:
    print(-1)
else:
    print(m)'''

#find the largest even number and smallest odd number [3,5,6,1,8,9] even 8 odd 1
'''l=list(map(int,input().split()))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(max(even))
print(min(odd))'''

#greedy approach
'''a=[1,3,4,2,8,5]
m=0
m1=99999 #to check min num
for i in a:
    if(i>m and i%2==0):
        m=i
    if(i<m1 and i%2!=0):
        m1=i
print(m,m1)'''
        
#second largest
a=[1,3,4,2,8,5]
f=0
s=0
for i in a:
    if(i>f):
        s=f
        f=i
    elif i>s and i!=f:
         s=i
print(s)


        
