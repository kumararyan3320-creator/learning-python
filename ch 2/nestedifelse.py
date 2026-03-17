# using nested if-else statement
# comparing n1 and n2

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 > n2:
    # either n1 or n3 is greatest
    if n1 > n3:
        print(n1, "is the greatest element")
    else:
        print(n3, "is the greatest element")
else:
    # either n2 or n3 is greatest
    if n2 > n3:
        print(n2, "is the greatest element")
    else:
        print(n3, "is the greatest element")




     