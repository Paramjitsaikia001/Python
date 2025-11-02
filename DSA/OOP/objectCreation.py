class Human:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    
    def __str__(self):
        return "the person name is " + self.name + " and age is " + str(self.age)
    
    def __repr__(self):
        return " person name is " + self.name + " and age is " + str(self.age)
    
h=Human(3,"paramjit saikia")
help(Human)
print(h)
        