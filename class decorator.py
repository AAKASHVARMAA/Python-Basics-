class Person:
    name="anonymous"
    @classmethod
    def personName(cls,name):
        cls.name=name

p1=Person()
p1.personName("abcd")
print(p1.name)