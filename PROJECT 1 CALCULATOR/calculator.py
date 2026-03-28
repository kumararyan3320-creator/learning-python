def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def mod(a, b):
    if b == 0:
        return "Error: Cannot mod by zero"
    return a % b

def floor_div(a, b):
    if b == 0:
        return "Error: Cannot floor divide by zero"
    return a // b

def power(a, b):
    return a ** b


while True:
    print("\n=== Python Calculator ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Floor Division (//)")
    print("7. Power (**)")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == "8":
        print("Exiting calculator...")
        break

    if choice not in ["1","2","3","4","5","6","7"]:
        print("Invalid choice! Try again.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = sub(a, b)
    elif choice == "3":
        result = mul(a, b)
    elif choice == "4":
        result = div(a, b)
    elif choice == "5":
        result = mod(a, b)
    elif choice == "6":
        result = floor_div(a, b)
    elif choice == "7":
        result = power(a, b)

    print("Result:", result)