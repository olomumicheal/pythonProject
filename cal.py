#a function that add two numbers
def add(x, y):
    return x + y

#a function that subtract two numbers
def subtract(x, y):
    return x - y

#a function that multiply two numbers
def multiply(x, y):
    return x * y

#a function that divide two numbers
def divide(x, y):
    return x / y

print("Select Operation :")
print("1. Add ")
print("2. Subtract")
print("3. Multiplication")
print("4. Division ")

#Creating input operation
choice = input("Enter a choice(1, 2, 3, 4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#implementing our functions
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("invalid number")






