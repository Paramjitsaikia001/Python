def insert(a):
    n=len(a)
    for i in range(n):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
            else:
                break
    return a

'''
TC=0(n^2)
SC=0(1)
'''
print(insert([-5, 3, 2, 1, -3, -3, 7, 2, 2]))