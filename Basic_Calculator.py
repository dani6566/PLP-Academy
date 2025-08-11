num1 = float(input("Enter the first number: "))
operation = input("Enter operation (+, -, *, /): ").strip()
num2 = float(input("Enter the second number: "))

def calculator(num1,num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation")


print(f"{num1} {operation} {num2} = {round(calculator(num1,num2),2)}")