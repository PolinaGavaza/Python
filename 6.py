import random
import math

def mini_calculator():
    operation = input("Введите операцию (+, -, /, *, **, %, rand, !, acos): ")
    if operation == "rand":
        print(random.randint(0, 100))
    elif operation == "!":
        num = int(input("Введите число: "))
        print(math.factorial(num))
    elif operation == "acos":
        num = float(input("Введите число: "))
        print(math.acos(num))
    else:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "/":
            print(num1 / num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "**":
            print(num1 ** num2)
        elif operation == "%":
            print(num1 % num2)
        else:
            print("Неверная операция")

mini_calculator()

