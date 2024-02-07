# WAP to find the greatest of 3 numners entered by the user
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if(num1>num2 and num1>num3):
    print("the greatest number is: ",num1)
elif(num2>num3):
    print("the greatest number is: ",num2)
else:
    print("the greatest number is: ",num3)