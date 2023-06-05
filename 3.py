
import math
import random


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  #Функция для вычисления факториала

def arccos(x):
    return math.acos(x)   #Функция для вычисления арккосинуса


operation = input("Введите операцию (+, -, /, *, ^, mod, rand, !, arccos): ") #Получаем операцию от пользователя

# Выполняем операцию в зависимости от выбора пользователя
if operation == "+":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(num1 + num2)
elif operation == "-":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(num1 - num2)
elif operation == "/":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(num1 / num2)
elif operation == "*":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(num1 * num2)
elif operation == "^":
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите степень: "))
    print(num1 ** num2)
elif operation == "mod":
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите модуль: "))
    print(num1 % num2)
elif operation == "rand":
    num1 = float(input("Введите максимальное значение: "))
    print(random.randint(0, num1))
elif operation == "!":
    num1 = int(input("Введите число: "))
    print(factorial(num1))
elif operation == "arccos":
    num1 = float(input("Введите число: "))
    print(arccos(num1))
else:
    print("Неверная операция")
