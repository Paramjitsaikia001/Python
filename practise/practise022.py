#define a class with radius using constructor create methods for area and parameter

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        # return 3.14*self.radius*self.radius
        return 3.14*self.radius**2
    
    def parameter(self):
        return 2*3.14*self.radius
    
C1=Circle(5)
print("Area of circle with radius ",C1.radius," is : ",C1.area()," and parameter is : ",C1.parameter())