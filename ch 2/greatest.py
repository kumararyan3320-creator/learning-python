n1 = int(input("Enter number1:"))
n2 = int(input("Enter number2:"))
n3 = int(input("Enter number3:"))

# if n1 is greatest
if n1 > n2 and n1 > n3:
    print(n1, "is the greatest number")
 # if n2 is greatest number
elif   n2 > n1 and n2 > n3:
    print(n2, "is the greatest number")
# if n3 is greatest number
else:
    print(n3, "is the greatest number")    
