"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def divide_numbers(num1, num2):
    try:
        print(round(num1 / num2, 3))
    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')



num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))

divide_numbers(num1, num2)
