a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))

if a>b and a>c :
   largest = a 
elif b>a and b>c:
   largest = b 
else:
   largest = c 
   print("Largest Number is : ",largest)
   
