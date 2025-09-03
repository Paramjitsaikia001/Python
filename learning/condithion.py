age=int(input("enter your age :"))
if(age<=11 and age>0):
    print("you are a child")#space is called indentation
elif(age>=12 and age<=18):
    print("you are a teenager")
elif(age>18):
    print("you are adult")
else:
    print("you are not born")
