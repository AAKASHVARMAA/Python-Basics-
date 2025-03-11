class Vehical:
    def start(self):
        print("Car Started")
    def stop(self):
        print("car stoped")
class Toyatocar(Vehical):
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def run(self):
        print("Car running")

class Fortuner(Toyatocar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("petrol")
car1.start()
car1.run()


