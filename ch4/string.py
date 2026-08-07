# String in Python can be defined using single quotes, double quotes, or triple quotes.
name1 = 'ARYAN'
name2 = "Aryan"
name3 = '''Aryan'''
# print(name1, name2, name3)
# print(type(name1), type(name2), type(name3))

# #Assigning multiline string to a variable
# multiline_string = '''This is a multiline string.
# It can span multiple lines.'''
# print(multiline_string)

#indexing in a string
# name = "Aryan"
# print(name[0]) #access the first character of the string
# print(name[-1]) #access the last character of the string

# #Traversing a string using a for loop
# for i in name1:
#     print(i)

# #List comprehension to create a list of characters in a string    
# list = [char for char in name1]
# for i in list:
#     print(i)

# #find the length of a string
# print(len(name1))

#find a char/substring in a string
# print(name1.find('A')) #check if 'A' is in name1
# print(name1.find('A', 1)) #check if 'A' is in name1 starting from index 1
# print(name1.find('YAN')) #check if 'YAN' is in name1
# print(name1.find('Z')) #check if 'Z' is in name1

#slicing in a string
#A R Y A N
#0 1 2 3 4
print(name1[2:4]) #access the characters from index 2 to 3 (4 is not included)
print(name1[-3:])