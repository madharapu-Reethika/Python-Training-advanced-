#BIT MANIPULATION
#n=int(input())
# if n&1==0:
#     print('even')
# else:
#     print('odd')
#     
# if n^1==n+1:
#     print('even')
# else:
#     print('odd')

#5---->1^2^3^4^5

# s=0   O(n)
# for i in range(1,n+1):
#     s=s^i
# print(s)

#OR

# if n%4==1: O(1)
#     print(1)
# elif n%4==2:
#     print(n+1)
# elif n%4==3:
#     print(0)
# else:
#     print(n)

# 5  10 ---->5^6^7^8^9^10
# n=int(input())
# m=int(input())
# s=0
# for i in range(n,m+1):
#     s=s^i
# print(s)
#OR
# def n_xor(n):
#     if n%4==1:
#         return 1
#     elif n%4==2:
#         return n+1
#     elif n%4==3:
#         return 0
#     else:
#         return n
# n=int(input())
# m=int(input())
# print(n_xor(n-1)^n_xor(m))


# power of two or not
n=int(input())

# if n &(n-1)==0: #o(1)
#     print('yes')
# else:
#     print('No')

#OR
# i=0
# while 1:  #o(logn)
#     if 2**i==n:
#         print('yes')
#         break
#     if n<2**i:
#         print('no')
#         break
#     i+=1

#or

# while n%2==0:   #O(logn)
#     n=n//2
# if n==1:
#     print('Yes')
# else:
#     print('No')

#sliding window
list=[2,2,4,4,6,6,7,7,8,8,9]
for i in range(0,len(list)-1,2):
    if list[i]!=list[i+1]:
        print(list[i])
        break

