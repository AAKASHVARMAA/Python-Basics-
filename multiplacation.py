number=int(input("Enter the number: "))
i=1
for i in range(1,11):
    i*=number
    print(i)
    i+=1

number2=int(input("enter the number2:"))
res=1
while number2>1:
    res*=number2
    number2-=1
print(res)