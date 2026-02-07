def quicksort(a):
    n=len(a)
    if n<=1:
        return a
    p=a[-1]

    l=[x for x in a[:-1] if x <=p]
    r=[x for x in a[:-1] if x>p]

    l=quicksort(l)
    r=quicksort(r)

    return l+[p]+r

'''
time complexity =0(nlogn)
space complexity=0(n)
'''
print(quicksort([-5, 3, 2, 1, -3, -3, 7, 2, 2]))
