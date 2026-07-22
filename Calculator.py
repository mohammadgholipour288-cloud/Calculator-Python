num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
operator = input("Enter the operator:\n")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
else:
    print(num1 // num2)