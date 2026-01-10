
#creating a binary tree

class bt:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.val)

'''
          1
    2          3
4       5   10

'''



a=bt(1)
b=bt(2)
c=bt(3)
d=bt(4)
e=bt(5)
f=bt(10)

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f


# print(a)






#DFS
'''
Pre order recursion 
TC=0(n)
SC=0(n)

'''

def pre_order(node):

    #base case if node is empty
    if not node:
        return 
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

print("pre order recursion:")
pre_order(a)



'''
In order recursion 
TC=0(n)
SC=0(n)

'''

def in_order(node):

    #base case if node is empty
    if not node:
        return 
    
    in_order(node.left)
    print(node)
    in_order(node.right)

print("in order recursion:")
in_order(a)




'''
Post order recursion 
TC=0(n)
SC=0(n)

'''

def post_order(node):

    #base case if node is empty
    if not node:
        return 
    
    post_order(node.left)
    post_order(node.right)
    print(node)

print("post order recursion:")
post_order(a)



#DFS
'''
Pre order interative 
TC=0(n)
SC=0(n)

'''

def pre_order_iterative(node):

    #base case if node is empty
    stk=[node]
    while stk:
        n=stk.pop()
        if n.right:stk.append(n.right)
        if n.left:stk.append(n.left)
        print(n)

print("pre order Interative :")
pre_order_iterative(a)




'''
Post order interative 
TC=0(n)
SC=0(n)

'''

def post_order_iterative(node):

    #base case if node is empty
    stk1=[node]
    stk2=[]
    while stk1:
        n=stk1.pop()
        stk2.append(n)
        if n.left:
            stk1.append(n.left)
        if n.right:
            stk1.append(n.right)
    while stk2:
        print(stk2.pop())

print("post order Interative :")
post_order_iterative(a)




'''
In order interative 
TC=0(n)
SC=0(n)

'''

def in_order_iterative(node):

    #base case if node is empty
    stk=[]
    cur=node
    while stk or cur:

        while cur:
            stk.append(cur)
            cur=cur.left
        cur=stk.pop()
        print(cur)
        cur=cur.right

print("in order Interative :")
in_order_iterative(a)




#BFS
from collections import deque
def bfs(node):

    #base case if node is empty
    Q=deque()
    Q.append(node)
    while Q:
        n = Q.popleft()
        print(n)
        if n.left:Q.append(n.left)
        if n.right:Q.append(n.right)

print("BFS :")
bfs(a)





#searching 

# tc=0(n)
# sc=0(n)

def search(node,target):
    if not node:
        return False
    if node.val==target:
        return True
    
    return search(node.left,target) or search(node.right,target)


print("searching in bt ",search(a,-1))