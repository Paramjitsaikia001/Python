# name = input("enter your name :")

#strip is a function and it removes all the whitespace of a string
#name = name.strip()

#capitlize the first letter of string
# name =name.capitalize()

#capitlize the first letter of each word
#name =name.title()

#we can write as
#name =name.strip().title()


#and also can write as
# name = input("enter your name :").strip().title()


fullname = input("enter you full name:").title()

firstName,lastName=fullname.split(" ")

print(f"the last name of  {firstName} is {lastName}")