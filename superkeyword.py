class Vehical:
    def __init__(self,type):
        self.type=type
    def start(self):
        print("Car Started")
    def stop(self):
        print("car stoped")
class Toyatocar(Vehical):
    def __init__(self,name,color,type):
        self.name=name
        self.color=color
        super().__init__(type)
        super().start()
c1=Toyatocar("fortuner","white","fuel")
print(c1.name)