import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b 

def modulo(a, b):
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Square root is not defined for negative numbers."
    return a ** 0.5

def log_base_10(a):
    if a <= 0:
        return "Error: Logarithm is not defined for numbers less than or equal to zero."
    return math.log10(a)

def log_base_e(a):
    if a <= 0:
        return "Error: Logarithm is not defined for numbers less than or equal to zero."
    return math.log(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def factorial(a):
    if not isinstance(a, int) or a < 0:
        return "Error: Factorial is only defined for non-negative integers."
    return math.factorial(a)

while True:
    try:
        operation = int(input("Select the operation you want to use:"
                              "\n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Modulo \n6. Power \n7. Square Root \n8. Log Base 10 \n9. Log Base e \n10. Sine \n11. Cosine \n12. Tangent \n13. Factorial\n"))
        if 1 <= operation <= 13:
            break
        else:
            print("Error: You must select a valid option.")
    except ValueError:
        print("Error: You must enter a valid integer.")

# Initialize 'result'
result = None

# Request numbers from the user based on the selected operation    
if operation in [1, 2, 3, 4, 5, 6]:  # Operations that require two numbers
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
elif operation in [7, 8, 9, 10, 11, 12, 13]:  # Operations that require one number
    a = float(input("Enter the number: "))
    if operation == 13:  # Only for factorial, convert to integer
        try:
            a = int(a)
        except ValueError:
            print("Error: The number must be an integer to calculate the factorial.")
            result = "Error: The number must be an integer to calculate the factorial."
else:
    result = "Error: Invalid operation."

# Call the function based on the selected operation
if result is None:
    if operation == 1:
        result = add(a, b)
    elif operation == 2:
        result = subtract(a, b)
    elif operation == 3:
        result = multiply(a, b)
    elif operation == 4:
        result = divide(a, b)
    elif operation == 5:
        result = modulo(a, b)
    elif operation == 6:
        result = power(a, b)  
    elif operation == 7:
        result = square_root(a)
    elif operation == 8:
        result = log_base_10(a)
    elif operation == 9:
        result = log_base_e(a)
    elif operation == 10:
        result = sine(a)
    elif operation == 11:
        result = cosine(a)
    elif operation == 12:
        result = tangent(a)
    elif operation == 13:
        result = factorial(a)

print(f"Result: {result}")
