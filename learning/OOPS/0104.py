class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showNumber(self):
        print("Complex number is : ",self.real ," + ",self.img ,"i")
    
    def __add__(self,num2):
        return complex(self.real+num2.real,self.img+num2.img)
    
c1=complex(3,4)
c1.showNumber()

c2=complex(4,1)
c2.showNumber()

c3=c1+c2

c3.showNumber()