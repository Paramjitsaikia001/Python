#implement the series of 1-2/2!+3/3!-.......n/n!


def fact(n):
    if n <=1:
        return 1
    else:
        return n*fact(n-1)

def series(n):
    if n ==1:
        return 1
    ans=0
    for i in range(1,n+1):
        print(ans)
        if i%2==0:
            ans-=i/fact(i)
        else:
            ans+=i/fact(i)
    return ans
        
print(series(3))