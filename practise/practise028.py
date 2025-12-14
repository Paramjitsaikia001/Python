class negativeNumberError(Exception):
    pass


x = int(input("enter a number: "))
try:
    if x<0:
        raise negativeNumberError

except negativeNumberError :
    print("number should be positive")
else:
    print("GOOD ! ",x)
finally:
    print("DONE ")
