import mymodule

print(mymodule.isEven(30))


# COUNT function is how can time a element there in the variable

nums=[2,34,1,6,23,66,12,10,3,5,1]

print("no. of 1's:",nums.count(1))


#COUNTER 
from collections import Counter

c =Counter(nums)

print("using counter in banana: ",c)
print("using counter in banana: ",c.most_common()) #it converted to the list from the dict