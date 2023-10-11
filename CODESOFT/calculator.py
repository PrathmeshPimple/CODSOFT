# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# for input of two numbers for user 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Arithmatic Expression :")
print("+ ->Addition")
print("- ->Subtraction")
print("* ->Multiplication")
print("/ ->Division")

# entering the operation to be implemented 
operation = input("Enter operation choice ( '+' | '-' | '*' | '/' ): ")

# Perform calculation based on user's choice
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation !"

# Display the result
print("Result: ",result)