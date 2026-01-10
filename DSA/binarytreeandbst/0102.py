class bt:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.val)

# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9



a=bt(5)
b=bt(1)
c=bt(8)
d=bt(-1)
e=bt(3)
f=bt(7)
g=bt(9)

a.left,a.right=b,c
b.left,b.right=d,e
c.left,c.right=f,g


def searchBST(node,target):
    if not node:
        return False
    
    if node.val==target:
        return True
    if target <node.val:
        return searchBST(node.left,target)
    else:
        return searchBST(node.right,target)



print(searchBST(a,3))