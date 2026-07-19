while True:
    
    First_number = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    Second_number = float(input("Enter the second number: "))
    
    if operation == "+":
        result = First_number + Second_number
        print(f"The result of {First_number} + {Second_number} is: {result}")

    elif operation == "-":
        result = First_number - Second_number
        print(f"The result of {First_number} - {Second_number} is: {result}")
        
    elif operation == "*":
        result = First_number * Second_number
        print(f"The result of {First_number} * {Second_number} is: {result}")
        
    elif operation == "/":
        if Second_number == 0:
            print("Error: Division by zero is not allowed.")
            
        else:
            result = First_number / Second_number
            print(f"The result of {First_number} / {Second_number} is: {result}")
        
    else:
        print("Error: Invalid operation.")
        
    Repeat = input("Do you want to perform another calculation? (yes/no): ")
    
    if Repeat == "no":
        print("Thank you for using the calculator. Goodbye!")
        break

    else:
        print("Please enter yes or no.")                