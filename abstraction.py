class Abstraction:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cltch = False

    def Car(self):
        self.cltch = True
        self.acc = True
        print("The car started")

car1=Abstraction()
car1.Car()