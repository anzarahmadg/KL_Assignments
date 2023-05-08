class Calculator:
    def addition(num1, num2):
        return num1 + num2
    def subtraction(num1, num2):
        return num1 - num2
    def division(num1, num2):
        return num1 / num2
    def multiplication(num1, num2):
        return num1 * num2
    
while True:
    print("____________Calculator______________")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): or q to quit ")
    
    if operator == "q":
        break
    elif operator == "+":
        print(Calculator.addition(num1,num2))
    elif operator == "-":
        print(Calculator.subtraction(num1,num2))
    elif operator == "*":
        print(Calculator.multiplication(num1,num2))
    elif operator == "/":
        print(Calculator.division(num1,num2))
    else:
        print("Invalid option")
        exit()