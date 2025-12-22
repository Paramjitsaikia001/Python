#fibonacci series
'''

NOTE 
 Time complexity of this function is 0(2^n) 
 space complexity of this function is 0(n)

'''
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(1):
    print(fibonacci(i))