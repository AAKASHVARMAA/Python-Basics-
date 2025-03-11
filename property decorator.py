class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
        
        
    #def clacpercentage(self):
        #self.per=str((self.math+self.phy+self.chem)/3)+"%"
    @property
    def Percentage(self):
        return str((self.math+self.phy+self.chem)/3) +"%"


stu=Student(98,97,96)
print(stu.Percentage)

