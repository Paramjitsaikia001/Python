class car:
    @staticmethod
    def start():
        print("starting...")
    
    @classmethod
    def type(cls,typeof):
        cls.typeof=typeof

c1 =car()
c1.start()
print("car is an ",c1.type("electrical"))