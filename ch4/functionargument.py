def add(a, b):   # a, b = parameters
    return a + b

add(2, 3)        # 2, 3 = arguments
print


# def greet(name, age):
#     print(name, age)

# greet("Aryan", 20)  # positional arguments
# greet(age=20, name="Aryan")  # keyword arguments


# def greet(name, age):
#     print(name, age)

# greet("Aryan", 18) # positional arguments
# greet(age=18, name="Aryan") # keyword arguments

#default arguments
def greet(name, age=18):
    print(name, age)

greet("Aryan")  # uses default age
greet("Aryan", 20)  # overrides default age
#
def say(message, times = 1):
    print(message * times)

say('Hello')
say('World', 5)




