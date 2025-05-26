class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def add_back(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end='->')
            t=t.next
        print('None')
    def sum(self):
        t=self.head
        s=0
        while(t!=None):
            s=s+t.data
            t=t.next
        print(s)
    def sumeven(self):
        t=self.head
        s=0
        while(t!=None):
            if t.data%2==0:
                s=s+t.data
            t=t.next
        print(s)
    def evenposition(self):
        t=self.head
        s=0
        pos=1
        while(t!=None):
           if pos%2==0:
               s=s+t.data
           t=t.next
           pos+=1
        print(s)     
    def secondmax(self):
        t=self.head
        max=0
        max2=0
        while(t!=None):
            if t.data>max:
                max2=max
                max=t.data
            elif t.data!=max and t.data>max2:
                max2=t.data
            t=t.next
        print(max2)
    def consecutive(self,k):
        t=self.head
        c=0
        while(t.next!=None):
            s= t.data + t.next.data
            if s<=k:
                c+=1
            t=t.next
        print(c)
    def allposipair(self,k):
           t=self.head
           c=0
           while(t.next!=None):
               t2=t.next
               while t2!=None:
                   s=t.data+t2.data
                   if s<=k:
                       c+=1
                   t2=t2.next
               t=t.next    
           print(c)
    def secondhalf(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None): #even length and odd length
            f=f.next.next
            s=s.next
        while s!=None:
            print(s.data,end='->')
            s=s.next
        print(None)
    def firsthalf(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            f=f.next.next
            print(s.data,end='->')
            s=s.next
        print(None)
    def knodelast(self,k):
        f=self.head
        s=self.head
        for i in range(k):
            f=f.next
        while(f!=None):
            f=f.next
            s=s.next
        print(s.data)
    def delknodelast(self,k):
         f=self.head
         for i in range(k):
             f=f.next
         s=self.head
         while(f!=None):
             prev=s
             s=s.next
             f=f.next
         prev.next=s.next
    def swap(self):
        t=self.head
        while t!=None and t.next!=None:
            t.data,t.next.data=t.next.data,t.data
            t=t.next.next
    def bubblesort(self):
        Flag=True
        while Flag:
            t=self.head
            Flag=False
        while t!=None and t.next!=None:
            if t.data>t.next.data:
                t.data,t.next.data=t.next.data,t.data
                Flag=True
            t=t.next
#kth largest element in unsorted list            
    def kthlaele(self,k):
        temp=self.head
        k1=k
        while temp!=None:
            f=0
            curr=self.head
            while curr.next!=None:
                if curr.data>curr.next.data:
                    f=1
                    curr.data,curr.next.data=curr.next.data,curr.data
                curr=curr.next
            if f==0:
                break
            temp=temp.next
            k-=1
        self.knodelast(k1)
#to check loop in a linkedlist        
    def checkloop(self):
        f=self.head
        s=self.head
        while(f!=None and f.next!=None):
            
            f=f.next.next
            s=s.next
            if f==s:
                print('loop')
                return
        print('no loop')                          
'''                                    
l1=linked()
l1.head=node(9)
l1.add_back(3)
l1.add_back(10)
l1.add_back(11)
l1.add_back(2)
l1.add_back(5)
l1.display()
l1.sum()
l1.sumeven()
l1.evenposition()
l1.secondmax()
l1.consecutive(50)
l1.allposipair(50)
l1.secondhalf()
l1.firsthalf()
l1.knodelast(3)
l1.delknodelast(3)
l1.display()
l1.swap()
l1.display()
l1.bubblesort()
l1.display()
l1.kthlaele(2)
l1.checkloop()'''
l2=linked()
l2.head=node(100)
l2.head.next=node(200)
l2.head.next.next=node(300)
l2.head.next.next.next=node(400)
l2.head.next.next.next.next = l2.head.next
l2.checkloop()




        
        

