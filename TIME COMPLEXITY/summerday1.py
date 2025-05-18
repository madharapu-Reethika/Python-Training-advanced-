#TIME COMPLEXITY
#prime number
'''n = int(input())
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f'not {n} a prime number')
            break
    else:
        if n > 200:
            print(f'yes {n} greater than zero')
        else:
            print('prime but less than 200')
else:
    print(f'not {n} a prime number')'''


'''def dup(list):
    l2=[]
    
    for i in list:
        if i not in l2:
            l2.append(i)
    return l2        
list=[8,2,3,4,3,3,4,5,6,7,9,2,4]
print(*dup(list))       
  
#o(n**2)'''

'''a=7
a=a-2
b=0
b=b+1+1
b=b-1
c=a^b
print(c)'''

'''n=5
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''

#sum of n number
'''n=5
natural=n*(n+1)//2
print(natural)'''

'''n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)'''

'''lst=[2,6,4,6,7,3,2,6,8]
s=0
for i in range(0,len(lst),2):
        s=s+lst[i]        
print(s)'''        

'''n=40
i=1
while (i<n):
    print('hi')
    i=i*2'''

#two pointer approach
'''a=[2,4,5,7,8]
b=[3,5,6,10,11,12,14]'''


'''lst = [2, 3, 4, 3, 2, 5, 5]
for i in lst:
    if lst.count(i) < 2:
        print(i)'''

'''from collections import Counter
lst = [2, 3, 4, 3, 2, 5, 5]
freq = Counter(lst)
for i in lst:
    if freq[i] < 2:
        print(i)'''
        
li=[2,3,4,3,2,5,5]
d={}
for c in li:
    if c not in d:
        d[c]=1
    else:
        d[c]+=1
for k,v in d.items():
    if v<2:
        print(k) 

'''a=[2,3,4,3,2,5,5]
s=0
for i in a:
    s=s^i
print(s)'''    










        
        