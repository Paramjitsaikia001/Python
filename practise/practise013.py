# WAP  to find the sum of first n natural numbers(using while)

x= int(input("enter a number:"))

sum=0
i=1
while i <=x:
    sum+=i
    i+=1

print(f"sum of ${x} number :{sum}")