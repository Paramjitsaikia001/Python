mark=int(input("enter your mark:"))
if(mark>=90):
    print("Grade= A ")
elif(mark>=80 and mark<90):
    print("Grade= B ")
elif(mark<80 and mark>=70):
    print("Grade= C ")
else:
    print("Grade= D ")