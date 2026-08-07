# # write a function that prints hello world

# def printHello():
#     # body of function
#     print("Hello world!!")
# #👉 Is stage par function sirf memory me store hota hai
# #👉 Ye run nahi hota ❌

# printHello()
# #👉 Ye line function ko execute karti hai
# #👉 Tab output aata hai ✔

#function which takes 2 numbers as input and prints their sum
def add(n1, n2=0):
    print("n1 is ", n1) #for self checking
    print("n2 is ", n2) #for self checking
    sum = n1 + n2 
    return sum#👉 return statement se function ke andar ka result bahar aata hai

#positional aurguments
print("sum is ", add(2, 3))

#keyword arguments (named arguments)
print("The sum is ", add(n2 = 3, n1 = 2))

#defult arguments
print("The sum is ", add(3))