# n = int(input("Enter n: "))
# for i in range(n):
#     print("*" * 5)



# n = int(input("Enter n: "))
# for i in range(n):       # i use for rows
#     for j in range(1, n + 1):    # j use for columns
#         print(j, end="")  # end="" is used to print in the same line
#     print()  # print() is used to move to the next line



# n = 4
# for i in range(1, n + 1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# n = 7
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print(i , end="")
#     print()


# for i in range(5):
#     for j in range(i):
#         print(i , end="")
#     print()


# for i in range(7):
#     for j in range(i + 1):
#         print(i , end="")
#     print()


# for i in range(5):
#     for j in range(i + 1):
#         print("*" , end="")
#     print()

n = 4
for i in range(1, n + 1): #loof for rows
   #print space 
   print(" " * (n - i), end="")
   #print digits
   for j in range(1, 2 * i):
       print(j, end="")
   print()