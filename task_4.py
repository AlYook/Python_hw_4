"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
"""


def my_func(x, y):
    positive_y = y * -1

    c = 1

    for num in range(positive_y):
        c *= x

    return 1 / c



print(my_func(5, -1))
print(my_func(4, -12))
print(my_func(12, -3))
