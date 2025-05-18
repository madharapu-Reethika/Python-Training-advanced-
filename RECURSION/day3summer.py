#recursion
'''def q(x):
    if(x==6): #base case
        return
    print('hi',x) #first function call to last
    q(x+1)
    print('hi',x) #calls the recent function.last to firstw
q(1)'''

'''
def even_sum(x,i):
    if i==len(x):
        return 0
    if x[i]%2==0: #only even the element will be moved
        return x[i]+ even_sum(x,i+1) #even sum to increase i value
    else:
        return even_sum(x,i+1) #not even also i will move
    
a=[2,5,6,7,2,1,4,3,6]
print(even_sum(a,0))'''
'''
def reve(rev,n):
    if n==0:
        return rev
    else:
        return reve(rev*10+n%10,n//10)
print(reve(0,153))'''

#prime number
'''n=13
for i in range(2,(n//2)+1):
    if(n%i==0):
        print('np')
        break
else:
    print('p')
    '''
#count of prime numbers
#[13,17,21,23,22,7,29]
'''def isprime(i,x):
    if(i==(x/2)+1):
        return True
    if(x%i==0):
        return False
    return is_prime(i+1,x)
def countprime(x,i,c):
    if(i==len(x)):
        return c
    if(is_prime(2,x)):
        return countprime(x,i+1,c+1)
    is_prime(2,x)
a=[13,17,21,23,22,7,29]    
print(countprime(a,0,0)'''

#whether on substraction with 3 or 5 will i reach 1
x=20
flag=False
for _ in range(x):
    if x==1:
        flag=True
        break
    if x-3>=1:
        x-=3
    elif x-5>=1:
        x-=5
if flag:
    print('True')
else:
    print('False')


    





