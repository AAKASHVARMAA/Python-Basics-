class Average_Marks:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getAvg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("The average marks is ",sum/3)
            
    @staticmethod  #static method
    def hello():
        print("this is a decorator")
student1=Average_Marks("abcd",[50,90,80])
student1.getAvg()
Average_Marks.hello()