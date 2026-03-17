num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))

operator = input("Enter operator")

match operator:
    case"+":
        print("sum is ", num1 + num2)
    case"-":
        print("subtract is ", num1 - num2)  
    case"*":
        print("multiply is ", num1 * num2)   
    case"/":
        print("division is ", num1 / num2)    
    case _:
        print("Enter a valid operator")    

'''num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")'''

'''a = 10
b = 5
op = "+"

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")'''

'''day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")'''
