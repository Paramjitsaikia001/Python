# WAP to check if a list contains a palindrome of elements

# name =[1,2,4,2,1]
# print(list(reversed(name)))
# if name == list(reversed(name)):
#     print("its palindrome")
# else:
#     print("its not palindrome")


name =[1,2,4,2,1]
copy=name.copy()
copy.reverse()
if name == copy:
    print("its palindrome")
else:
    print("its not palindrome")