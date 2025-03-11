class Vehical:
    def start(self):
        print("Car Started")
    def stop(self):
        print("car stoped")
class Toyatocar(Vehical):
    def __init__(self,name,color):
        self.name=name
        self.color=color

car1=Toyatocar("Fortuner","Blue")
car2=Toyatocar("prius","Red")

print(car1.start())