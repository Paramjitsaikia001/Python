class singlylist:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        return str(self.val)
    
head=singlylist("head")
one=singlylist(3)
two=singlylist(6)
three=singlylist(9)
four=singlylist(12)

head.next = one
one.next=two
two.next=three
three.next=four
print(head)

# add at the end of the list
def add_at_end(head,i):
    new_node=singlylist(i)
    cur = head
    while cur.next:
        cur=cur.next
    cur.next=new_node
    return head


#add at the start of the list
def add_at_start(head,i):
    new_node=singlylist(i)
    new_node.next = head.next
    head.next=new_node

    return head


#traversing- TIME COMPLEXITY IS 0(n)
def traversal(head):
    cur =head
    result=[]
    while cur:
        result.append(str(cur.val))
        cur=cur.next
    print(" -> ".join(result))


#insert a element in a specific position
def insert(head,val,pos):
    new_node=singlylist(val)
    cur=head
    count=1
    if pos == 1:
        new_node.next=head.next
        head.next=new_node
        return head
    while cur.next and count < pos:
        cur = cur.next
        count+=1
    new_node.next=cur.next
    cur.next=new_node
    return head

# def insert(head,val,pos):
#     new_node=singlylist(val)
#     cur=head
#     count=1
#     if pos == 1:
#         new_node.next=head.next
#         head.next=new_node
#         return head
#     while cur or count <= pos:
#         if pos==count and cur:
#             new_node.next=cur.next
#             cur.next=new_node
#             return head
#         if not cur.next:
#             cur.next=new_node
#             return head
#         cur = cur.next
#         count+=1

insert(head,23,1)
insert(head,30,2)
# add_at_start(head,1)
# add_at_end(head,14)
traversal(head)