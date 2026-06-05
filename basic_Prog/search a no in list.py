#creating a tuple of square numbers by taking input from the user

a=int(input("enter the number till which you want the squares : "))
f=[]

while a>0:
    b=a*a
    f.append(b)
    a-=1
    print(b)

#asking the user which number is to be found
d=int(input("enter the number to be searched : "))

#extracting each element of the tuple and then comparing it with 
#the number to be found

i=0 
while i<len(f):
     e=f[i]
     if e==d:
        print(e ,"at index" ,i)
        u=True
        break
     
     i+=1

if not u:
    print("not found") 





