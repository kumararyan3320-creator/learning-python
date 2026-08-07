# ==============================
# 1. Creating a Dictionary
# ==============================
student = {
    "name": "Aryan",   # key = "name", value = "Aryan"
    "age": 20,         # key = "age", value = 20
    "marks": 85        # key = "marks", value = 85
}

# ==============================
# 2. Accessing Values
# ==============================
print(student["name"])        # Direct access (gives error if key not found)
print(student.get("age"))     # Safe access (returns None if key not found)

# ==============================
# 3. Adding New Element
# ==============================
student["city"] = "Lucknow"   # New key-value added

# ==============================
# 4. Updating Existing Value
# ==============================
student["age"] = 21           # Value updated

# ==============================
# 5. Length of Dictionary
# ==============================
print(len(student))           # Total number of key-value pairs

# ==============================
# 6. Looping Through Dictionary
# ==============================
for key, value in student.items():   # items() gives (key, value)
    print(key, ":", value)

# ==============================
# 7. Checking Key Exists or Not
# ==============================
print("name" in student)      # True if key exists

# ==============================
# 8. Removing Elements
# ==============================
student.pop("marks")          # Removes key "marks"
# student.popitem()           # Removes last inserted item
# del student["name"]         # Deletes specific key
# student.clear()             # Removes all elements

# ==============================
# 9. Using get() with Default Value
# ==============================
print(student.get("phone", "Not Found"))  # If key not found → returns "Not Found"

# ==============================
# 10. Dictionary Methods
# ==============================
print(student.keys())     # Returns all keys
print(student.values())   # Returns all values
print(student.items())    # Returns all (key, value) pairs

# ==============================
# 11. Nested Dictionary
# ==============================
students = {
    "s1": {"name": "Aryan", "age": 20},
    "s2": {"name": "Rahul", "age": 21}
}

print(students["s1"]["name"])  # Access nested value

# ==============================
# 12. Final Dictionary Output
# ==============================
print(student)





# Given dictionary

d = {'a': 100, 'b': 200, 'c': 300}
print("The sum of d value is ",sum(d.values()))

d = {
    'a': 100,
    'b': 200,
    'c': 300
}
print(d.values())




#Write a Python program to perform mirror operation on a string.
#Given a string and a number N, convert all characters from the N-th position to the end of the string into their mirror characters in the alphabet.
s = "pneumonia"
N = 6

result = ""

for i in range(len(s)):
    if i < N - 1:
        result += s[i]
    else:
        result += chr(ord('a') + ord('z') - ord(s[i]))

print(result)

