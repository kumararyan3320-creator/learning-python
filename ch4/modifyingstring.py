#for coverting characters to uppercase
str1 = "new york"
str2 = str1.upper() #create a new string with all characters in uppercase
print(str2)

#coverting characters to lowercase
str3 = str2.lower() #create a new string with all characters in lowercase
print(str3)

#capitalize the first character of the string
str4 = str3.capitalize() #create a new string with the first character capitalized
print(str4)

#strip() is used to remove leading and trailing whitespace from a string
str1 = "   Hello World!   "
print(str1.strip()) #remove leading and trailing whitespace

#replace() is used to replace occurrences of a specified substring with another substring
str1 = "I like apples"
str2 = str1.replace("apples", "oranges") #create a new string with "apples" replaced with "oranges"
print(str2)

str1 = "Hello World, what a beautiful world this is!"
print(str1.replace("world", "universe", 1)) #replace only the first occurrence of "world" with "universe"