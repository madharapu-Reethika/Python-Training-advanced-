#petriol question while every jump petrol it will be -1 if next element less than the element after minus replace
#[2,2,1,0,1,3,0] [2,3,1,0,1,3,0]
#a=[2,2,1,0,1,3,0]-->not
'''a=[2,3,1,0,1,3,0]#-->yes
p=0
for i in range(len(a)):
    if p<0:
        print('not possible')
        break
        
    p=max(p,a[i])
    p-=1
else:
    print('possible')'''

#jump game 2:
'''nums=[2,3,1,1,4]    
m=0
c=0
end=0
for i in range(len(nums)-1):
    if i>m:
        break
    if i+nums[i]>m:
        m=i+nums[i]
    if i==end:
        c+=1
        end=m
print(c)'''

#lemonade change
'''bills=[5,5,5,10,20]
five=ten=0
for i in bills:
    if i==5:
        five+=1
    elif i==10:
        if five>0:
            ten+=1
            five-=1
    else:
        return False
    elif i==20:
        if five>0 and ten>0:
            five-=1
            ten-=1
    elif five>=3:
        five-=3  
    else:
        return False
return True'''

#cpu scheduling
'''a=[4,3,7,1,6,2]
a.sort()
waittime=0
total=0
for i in range(len(a)-1):
    waittime+=a[i]
    total+=waittime
avg=total//len(a)
print(avg)'''

#bundle and business no of max business can happen
'''people=[1,6,2,3,4,5]
bundle=[4,2,3,1,1,2]
c=0
for i in people:
    for j in bundle:
        if i==j or i<j:
            c+=1
            break
print(c)'''

#assign cookies
'''g=[1,2,3]
s=[1,1]
g.sort()
s.sort()
c=i=0
j=0
while i<len(g)  and j<len(s):
        if s[j]>=g[i]:
            c+=1
            i+=1
        j=j+1
print(c)'''

#jump question minimum jump
'''nums=[2,3,1,1,4]    
m=0
c=0
end=0
for i in range(len(nums)-1):
    if i>m:
        break
    if i+nums[i]>m:
        m=i+nums[i]        
    if i==end:
        c+=1
        end=m
print(c)'''

#more optimized code jump sorting II
'''a=[2,3,1,1,4]
l=0
r=0
jump=0
f=0
while(r<len(a)-1):
    m=0
    for i in range(l,r+1):
        if(i+a[i]>m):
            m=i+a[i]
        if(m>len(a)-1):
            f=1
            break
    l=r+1
    r=m
    jump=jump+1
    if(f==1):
        break
print(jump)'''







        
    
    

