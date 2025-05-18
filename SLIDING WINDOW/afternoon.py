#sliding window
'''list = [2, 2, 4, 4, 6, 6, 7, 7, 8, 8, 9]
for i in range(0, len(list)-1, 2):
    if list[i] != list[i+1]:
        print(list[i])
        break
else:
    print(list[-1])'''

#count should be taken as 1
'''li = [1,2,3,2,3,4,5,6,7,8,9]
count = 1
maxcount = 1
for i in range(len(li) - 1):
    if li[i+1] - li[i] == 1:
        count += 1
        maxcount = max(maxcount, count)  
    else:
        count = 1  
print(maxcount)'''
'''
a = [1,2,3,2,3,4,5,6,7,8,9]
c = 1
max=1
for i in range(len(a)-1):
    if(a[i]+1==a[i+1]):
        c=c+1
    else:
        if (c>max):
            max=c
        c=1
if(c>max):
    max=c
print(max) '''

a='aaabbaaaacccddeff'
s=''
c=1
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        c+=1
    else:
         s=s+a[i]+str(c)
         c=1
s=s+a[i+1]+str(c)
print(s)
         
        

      
        
        
        
