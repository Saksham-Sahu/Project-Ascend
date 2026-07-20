# '''Greeting function'''
# def greeting(name):
#     return f"Hello, {name}! Welcome to our program."

# name = input("Please enter your name: ")
# print(greeting(name))

# '''Add function'''
# def add(a, b):
#     return a + b

# def if_even(number):   
#     if number % 2 == 0:
#         return True
#     else:
#         return False

def calculate_area(length, width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of the rectangle:", calculate_area(length, width), "square units")