#max profit using greedy O(n) leetcode buy and sell stock
#method 1
'''a=[13,14,2,5,8,1,4]
profit=0
buyp=a[0]
for i in range(1,len(a)):
    if a[i]>buyp:
        profit=max(profit,a[i]-buyp)
    else:
        buyp=a[i]
print(profit)'''

#maximum profit method 2
'''a=[13,14,2,5,8,1,4]
mp=0
p=a[0]
for i in range(1,len(a)):
    if a[i]>p:
        if a[i]-p>mp:
            mp=a[i]-p
        #mp=max(mp,a[i]-p)
    else:
        p=a[i]
print(mp)'''

#two pointer approach method 3
'''a=[13,14,2,5,8,1,4]
mp=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>mp:
            mp=a[j]-a[i]
print(mp)'''

#in a matrix calcuate the sum of numbers in a row above 1
#[8,7,6,5,2] [0 1 1 0 1] sum=13 [1 1 0 0 1] sum=17
'''a=[[0,1,1],[1,1,0],[1,1,0]]
b=[8,7,6]
n=3
for i in range(n):
    sum=0
    for j in range(n):
        if a[i][j]==1:
            sum+=b[j]
    print(sum) '''

#BACK TRACKING

#rat and maize total paths to reach last 
'''def rat(a,i,j,n):
    if(i==n or j==n or a[i][j]==0 ):
        return 0
    if (i==n-1 and j==n-1 and a[i][j]==1): # i+1 to go downside
        return 1   
    return rat(a,i,j+1,n)+rat(a,i+1,j,n)  # j+1 to go rightside
a=[[1,1,1],[1,0,1],[1,1,1]]
n=3
path=rat(a,0,0,n)
print(path)'''

#island problem
'''def land(a,i,j,n):
    if(i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2):
        return 0
    if(a[i][j]==1):
        a[i][j]=2
    land(a,i-1,j,n)
    land(a,i,j-1,n)
    land(a,i+1,j,n)
    land(a,i,j+1,n)
a=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
for i in a:
    print(i)
c=0    
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            land(a,i,j,5)
    c=c+1        
print(c) '''

#forest fire if one of the tree catch fire then remaining few trees will catch fire then count how many remaining were there
#refer again
'''def land(a,i,j,n):
    if(i==n or j==n or i<0 or j<0 or a[i][j]==0 or a[i][j]==2):
        return 0
    if(a[i][j]==1):
        a[i][j]=2
    land(a,i-1,j,n)
    land(a,i,j-1,n)
    land(a,i+1,j,n)
    land(a,i,j+1,n)
a=[[1,0,0,1,1],[1,0,0,0,1],[0,0,0,1,0],[1,0,0,0,0],[1,0,0,0,1]]
for i in a:
    print(i)
land(a,2,5,5)
c=0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:   
            c+=1        
print(c)'''

#there is a frog  and there are some hurdles and frog should not go there and the
#frog should reach last index matrix is 5 by 5 matrix tuple in the sense position of
#frog is 2,3 and the hurdles are (2,1),(4,1),(5,2),(3,5) output should be 7
'''def frog(n,i,j,hud):
    if(i==n or j==n or (i,j) in hud):
        return 0
    if('''

#n=3 print the binary numbers till n
'''import math
def allbinary(a,n,s=''):
    if a==-1:
        return a       
    if(len(s)==n):
        print(s)
        a=a-1
        return a
    a=allbinary(a,n,s+'0')
    a=allbinary(a,n,s+'1')
    return a
a=18
n=int(math.log(a,2))+1
allbinary(a,n,s='')'''

#open and closed brackets balanced
def all(n,s='',open=0,close=0):
    if len(s)==2*n:
        print(s)
        return
    if open<n:
        all(n,s+'(',open+1,close)
    if close<open:
        all(n,s+')',open,close+1)

n=3
all(n)
       







