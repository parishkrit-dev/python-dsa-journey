a=input("enter a list:").split()
print(a)
b=a[ : :-1]
print(b)
if a==b:
    print("list is plaindrome")
else:
    print("list is not a palindrome")
