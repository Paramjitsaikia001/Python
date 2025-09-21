# WAP to enter marks of 3 subjects from the use and store them in dictionary

marks={}
x = input("enter the marks of phy: ")
marks.update({"phy":x})
x = input("enter the marks of maths: ")
marks.update({"maths":x})
x = input("enter the marks of english: ")
marks.update({"english":x})

print(marks)
