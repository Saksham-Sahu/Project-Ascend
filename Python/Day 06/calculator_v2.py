def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
    

while True:
    
    a = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    b = float(input("Enter the second number: "))
    
    if operation == "+":
        add_result = addition(a, b)
        print("result is: ", add_result)
        
    elif operation == "-":
        sub_result = subtraction(a, b)
        print("result is: ",sub_result)
        
    elif operation == "*":
        mult_result = multiplication(a, b)
        print("result is: ", mult_result)
        
    elif operation == "/":
        div_result = division(a, b)
        print("result is: ", div_result)
        
    else:
        print("Error: Invalid operation.")

    repeat = input("Do you want to perform another calculation? (yes/no): ")

    if repeat == "no":
        print("Thank you for using the calculator. Goodbye!")
        break

    else:
        continue               