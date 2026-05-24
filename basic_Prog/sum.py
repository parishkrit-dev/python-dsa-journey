a=float(input("enter first numbers to be added : " ))
b=float(input("enter second numbers to be added : "))
s=a+b
s=round(s,2)
print("the sum of numbers is: ",s)

a,b=map(float,input("enter two numbers to be added : ").split())
s=a+b
s=round(s,2)
print("the sum of numbers is: ",s)