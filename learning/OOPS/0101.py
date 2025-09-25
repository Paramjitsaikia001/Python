# NORMAL CLASS-OBJECT

# class Student:
#     name="Paramjit saikia"

# s1=Student()
# print(s1.name)


# CONSTRUCTOR

class Student:
    
    def __init__(self,name):
        # print("hello from student class.")
        self.name=name

s1=Student("Paramjit Saikia")
print(s1.name)