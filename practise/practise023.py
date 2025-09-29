# create a class as employee set the role department salary using constructor and create a method to show the details. create another class as engineers that inherit the methods from the employee class and get method of age and name

class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        print("Role :",self.role)
        print("Department :",self.department)
        print("Salary :",self.salary)
    
class engineerr(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75,000")

    def showdetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        super().showdetails()

e=engineerr("Paramjit",22)
e.showdetails()