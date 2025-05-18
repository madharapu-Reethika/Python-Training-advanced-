#recusrion
'''def q(x,n,m):
    if x==1:
        return True  
    if(x<1):
        return False
    return q(x-n,n,m) or q(x-m,n,m)
x=4
n=3
m=5
print(q(x,n,m))'''

'''def q(x,n,m,c=0):
    if x==1:
        return 0
    if x<1:
        return False
    else:
        return 1+min(q(x-n,n,m,c+1),q(x-m,n,m,c+1))
x=20
n=3
m=5
print(q(x,n,m))'''

from collections import deque
def bfs(x, n, m):
    queue = deque()
    visited = set()
    queue.append((x, 0))   
    while queue:
        curr, steps = queue.popleft()
        if curr == 1:
            return True
        if curr < 1 or curr in visited:
            continue
        visited.add(curr)
        queue.append((curr - n, steps + 1))
        queue.append((curr - m, steps + 1))    
    return False
x = 4
n = 3
m = 5
print(bfs(x, n, m))


