# WAP to find the factorial of n numbers

x = int(input("enter n: "))

fac=1
for i in range(1,x+1):
    fac*=i

print(f"factorial of ${x} is ${fac}")
