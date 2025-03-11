class A:
    varA="Welcome to class A"
class B:
    VarB="Welcome to class B"
class C(A,B):
    VarC="Welcome to class C"

c1=C()
print(c1.varA)
