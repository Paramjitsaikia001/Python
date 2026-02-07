def selctionsort(a):
    n=len(a)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j
        a[i],a[min_idx]=a[min_idx],a[i]
    return a

'''
time complexity=0(n^2)
space complexity=0(1)
'''

print(selctionsort([-5, 3, 2, 1, -3, -3, 7, 2, 2]))