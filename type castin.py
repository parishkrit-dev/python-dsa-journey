a=float(input("enter string:"))
b=float(input("enter int"))
c=int(input("enter float"))
s=a+b+c
round(s) #rounds up the number ,remove round and youll understand y it is used
print(s)#prints a float value 
s=(type(s)) # now s does not contian a float value, it holds data type
print(s) #prints data type
print(type(a),type(b),type(c),type(s))
