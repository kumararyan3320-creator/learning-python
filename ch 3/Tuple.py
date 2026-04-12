colours = ("red", "green", "blue") #tuple is defined using parentheses
# print(colours)

# #creating a tuple with a single element
# fruit = ("apple",) #comma is required to create a single element tuple
# #check type of tuple
# print(type(fruit))
# #check length of tuple
# print(len(colours))
# print(len(fruit))

# #accessing elements of a tuple
# print(colours[0]) #access the first element of the tuple
# print(colours[-1]) #access the last element of the tuple
# print(fruit[0]) #access the first element of the single-element tuple
# #range of index
# print(colours[1:3]) #access the first two elements of the tuple
# print(colours[-2:]) #access the last two elements of the tuple

# #check if an item existis in the tuple
# if "red" in colours:
#     print("Yes, red is in the colours tuple")
# if "yellow" not in colours:
#     print("No, yellow is not in the colours tuple")

# #transverse the tuple using for loop
# for i in colours:
#     print(i)

# for i in range(len(colours)):
#     print(colours[i])

# concatenate two tuples
# colours1 = ("red", "green", "blue")
# colours2 = ("yellow", "orange", "purple")
# new_colours = colours1 + colours2
# print(new_colours)

# more_colours = ("pink", "brown")
# colours = colours + more_colours
# print(colours)

#unpacking a tuple
colours1 , colours2, colours3 = colours
print(colours1, colours2, colours3)