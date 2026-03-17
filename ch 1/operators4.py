# Arithmetic operators
# print("sum", 3 + 5)
# print("subtract", 5 - 4)
# print("multiply", 5 * 4)

# # Floor division ka use tab karte hai jab hame decimal value aaye
# # ye nearest whole number deta hai
# print("floor division", 5 // 2)

# Modulus ka use remainder nikalne ke liye hota hai
# print("modulus", 4 % 3)

# Exponentiation ka use power ke liye hota hai
# print("exponentiation", 5 ** 2)
# print("exponentiation", 5 ** 3)

# # Assignment operators
# n1 = 5
# n2 = n1
# print(n1, n2)

# n2 *= n1
# print(n1, n2)

# n1 = 2
# n2 = n1
# print(n1 ** n2)

# # Comparison operators
# n1 = 4
# n2 = 3
# print(n1 == n2)
# print(n1 != n2)
# print(n1 > n2)
# print(n1 < n2)
# print(n1 >= n2)
# print(n1 <= n2)

# Logical operators
# a = 20
# b = 30
# print(a > 15 and b > 25)
# print(a > 25 and b > 25)

# a = 10
# b = 20
# print(a > 15 or b > 15)
# print(a > 15 or b < 10)

# a = True
# print(not a)

# x = 10
# print(not x > 5)

# exp1 = 2 > 1
# exp2 = 5 < 4

# print(exp1 and exp2)
# print(exp1 or exp2)
# print(not exp1)

#  bina string use kiye bhi output print karwa sakte hai
#  string sirf label ke liye hoti hai
# print("exp1 and exp2:", exp1 and exp2)
# print("exp1 or exp2:", exp1 or exp2)
# print("not exp1:", not exp1)

# Identity operators
# x = 5
# y = 5
# print(x is y)
# print(x is not y)

# # both are same
# x = 6
# y = 6
# print("if x is y:", x is y)
# print("if x is not y:", x is not y)

# x = None
# if x is None:
#     print("No value")

# x = 10
# if x is None:
#     print("No value")

# Membership operators
# name = "ARYAN"
# print("A" in name)
# print("Z" in name)

# nums = [1, 2, 3, 4]
# print(2 in nums)
# print(6 in nums)
# print(4 in nums)

# print("A" not in name)
# print("Z" not in name)

# data = {"name": "Aryan", "age": 20}
# print("name" in data)     # True
# print("Aryan" in data)    # False Dictionary me in operator sirf keys ko check karta hai, values ko nahi
#  yaha sirf keys check hoti hai, values nahi

# fruits = ["apple", "banana", "cherry"]
# print("if banana is present in fruits:", "banana" in fruits)
# print("if mango is not present in fruits:", "mango" not in fruits)

# Bitwise operators
'''a = 5
b = 3
print("a and b:", a & b)
print("a or b:", a | b)
print("a xor b:", a ^ b)

#Binary me solve karke output
a = 12
b = 10
print("a and b:", a & b)

x = 7
y = 4
print("a or b:", x | y)

m = 9
n = 5
print("a xor b:", m ^ n)

num = 3
print("num:", num << 2)'''
a = [1, 2, 3]
b = a 
a = a + [4]
print(b)
