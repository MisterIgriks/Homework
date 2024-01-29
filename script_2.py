def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add(num1, num2)
diff_result = subtract(num1, num2)
prod_result = multiply(num1, num2)
div_result = divide(num1, num2)

print(f"Addition: {sum_result}")
print(f"Subtraction: {diff_result}")
print(f"Multiplication: {prod_result}")
print(f"Division: {div_result}")

