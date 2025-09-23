# WAP to print the elements of list
num=[1,2,3,4,5,6,7,8]


# def printList(list,n,i=0):
#     if i>=n:
#         return
#     print(list[i])
#     printList(list,n,i+1)

# printList(num,len(num))


def printList(list,i=0):
    if i ==len(list):
        return
    print(list[i],end=",")
    printList(list,i+1)

printList(num)
    