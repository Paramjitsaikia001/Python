class car:
    def __init__(self,type):
        self.type=type

    def start(self):
        print("engine starting....")
    
    def stop(self):
        print("engine stopping....")

class toyota(car):
     def __init__(self,name,type): #inheriting the variable from the parent class
        super().__init__(type)
        self.name=name
        print(self.name," is ",self.type," type car.")

c1=toyota("fortunar","electric")
c1.start()
