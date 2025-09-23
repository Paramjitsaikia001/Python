# recursion

n=12

def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fact(n-1) +fact(n-2)

for i in range(n+1):
    print(fact(i),end=",")