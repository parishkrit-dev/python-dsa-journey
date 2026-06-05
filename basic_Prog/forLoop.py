a=int(input("enter the number till where you want the squares : "))
list=[]
i=0
while i<=a:
    b=i*i
    list.append(b)
    i+=1
    print(b)

x=int(input("enter the number to be searched : "))

u=False
for idx,tup in enumerate(list):
     if tup==x:
          print(" found",tup,"at index",idx)
          u=True
          break

if u==False:
     print("not found")
    
