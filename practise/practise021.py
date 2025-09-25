# WAP to get name and marks of 3 subjects in the constructor of class and create a method to print the average of marks


class students:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def avg_result(self):
        sum=0
        for val in self.marks:
            sum+=val
            
        print(f"Hi,{self.name} Your score is : {sum/3:.2f}")

s1=students("Paramjit Saikia",[67,88,90])

s1.avg_result()