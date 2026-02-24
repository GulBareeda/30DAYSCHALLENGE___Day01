Result_1 = int(input("Enter your first number: "))
Operator = input("Enter any operator (+, -, *, %): ")
Result_2 = int(input("Enter your second number: "))

def Add(x, y):
    return x + y

def Multiply(x, y):
    return x * y

def Sub(x, y):
    return x - y

def Modulus(x, y):
    return x % y

valid_ops = ('+', '-', '*', '%')

if Operator not in valid_ops:
    print("Invalid operator")
elif Operator == '+':
    print(Add(Result_1, Result_2))
elif Operator == '*':
    print(Multiply(Result_1, Result_2))
elif Operator == '-':
    print(Sub(Result_1, Result_2))
elif Operator == '%':
    print(Modulus(Result_1, Result_2))
