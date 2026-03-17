'''for i in range(1, 6):
    print(i)

for i in range(6):
    print("Hello World")

for i in range(1, 12):
    print("Hello world")

for i in range(1, 12, 2):
    print("Hello world")

for i in range(10):
   print(i, "Hello world")

for i in range(1, 11, 2):
    print(i, "Hello world")'''


#print number from 1 to 5
'''i = 1
while i <= 5:
    print(i)
    i = i + 1'''
# A while loop is an iteration control structure that repeadtedly executes a block of code as long as a give condition is true 
#(like a list, tuple, etc.).

# print the even numbers from 1 to 10
'''i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i = i + 1
#print all even numbers from 1 to 20 also not mention if condition
i =  2
while i <= 20:
    print(i)
    i = i + 2

#predict the output of the following code
j = 0
while j <= 10:
    print(j)
    j = j + 1

x = 1
while x == 1:
    x = x -1
    print(x)
x = 4
y = 0
while x >= 0:
    x = x - 1
    y = y + 1
    print(x+y)'''

# x = 4
# y = 0

# while x >= 0:
#     x -= 1
#     y += 1
    
#     if x == y:
#         continue
#     else:
#         print(x + y)

''' ITERATION1
X = 4 -3
Y = 0 - 1
X!= y -> print
output: 3 + 1  = 4'''

''' ITERATION2
X =3 -2
Y = 1 -2
X!= y -> prinSKIP CONTINUET
output:nothing'''

''' ITERATION3
x=2 -1
y=2 -3
x!=y -> print
output: 1 + 3 = 4'''

''' ITERATION4
x = 1 -0
y = 3 -4
x!=y -> print
output: 0 + 4 = 4'''
''' ITERATION5
x = 0 -1
y = 4 -5
ab x>=0 false ho jayega to loop stop ho jayega'''
'''final output: 4 4 4'''


# x = 4
# y = 0
# while x >= 0:
#     if x == y:
#         break
#     else:
#         print(x + y)
#         x = x - 1 
#         y = y + 1
'''🔄 Dry Run (step by step):
🔹 Iteration 1:
x = 4, y = 0
x != y → else chalega
print → 4 + 0 = 4
x = 3
y = 1
👉 Output: 4
🔹 Iteration 2:
x = 3, y = 1
x != y → print
print → 3 + 1 = 4
x = 2
y = 2
👉 Output:


4
4
🔹 Iteration 3:
x = 2, y = 2
x == y → 🔥 break
👉 Loop turant band
👉 aage kuch nahi chalega
📌 Final Output:
4
4'''
    
# x = 4
# y = 0

# while x >= 0:
#     if x == y:
#         break
#     else:
#         print(x, y)
    
#     x = x - 1
#     y = y + 1
'''🔄 Dry Run (step by step):
🔄 Dry Run:
🔹 Iteration 1:
x = 4, y = 0
x != y → print
👉 Output: 4 0
x = 3
y = 1
🔹 Iteration 2:
x = 3, y = 1
x != y → print
👉 Output: 3 1
x = 2
y = 2
🔹 Iteration 3:
x = 2, y = 2
x == y → 🔥 break
👉 loop yahi stop
📌 Final Output:
4 0
3 1'''

#WAP a program  to print the square of the number from 1 to 5 using a while loop 
# i = 1 
# while i <= 5:
#     print(i**2)
#     i = i + 1
'''🎯 Core logic:
i 1 se start ho raha
har baar +1 ho raha
har number ka square print ho raha'''

#WAP to print number unit 5 using loop & stop when number becomes 6

# i = 1
# while i <= 10:
#     if i == 6:
#         break
#     else:
#         print(i)
#     i = i + 1
'''🔹 Step 1:
i = 1
condition: 1 <= 10 ✅
👉 print → 1
👉 check: 1 == 8 ❌
👉 i = 1 + 1 = 2
🔹 Step 2:
i = 2
condition: 2 <= 10 ✅
👉 print → 2
👉 check: 2 == 8 ❌
👉 i = 2 + 1 = 3
🔹 Step 3:
i = 3
👉 print → 3
👉 i = 4
🔹 Step 4:
i = 4
👉 print → 4
👉 i = 5
🔹 Step 5:
i = 5
👉 print → 5
👉 i = 6
🔹 Step 6:
i = 6
👉 print → 6
👉 i = 7
🔹 Step 7:
i = 7
👉 print → 7
👉 i = 8
🔹 Step 8:
i = 8
👉 print → 8
👉 check: 8 == 8 ✅
💥 break → loop yahi band'''