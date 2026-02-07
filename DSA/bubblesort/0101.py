def bubblesort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
        n-=1
    return a
"""
in this code , no flag use for if any part is sorted or not so then,
in the best case time complexity it will be 0(n2)
"""
def bubblesortflag(a):
    n=len(a)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if a[i]<a[i-1]:
                flag=True
                a[i],a[i-1]=a[i-1],a[i]
    return a
'''
in the above code we're using flag so,
in the best cases the time complexity will be 0(n)
'''
print("without flag : " , bubblesort([-5, 3, 2, 1, -3, -3, 7, 2, 2]))
print("with flag: ",bubblesort([-5, 3, 2, 1, -3, -3, 7, 2, 2]))
