"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()

    return nums[1] + nums[2]


def my_func_without_sort(num1, num2, num3):
    nums = [num1, num2, num3]

    min_num = min(nums)

    return sum(nums) - min_num



print(my_func(2, 4, 5))
print(my_func_without_sort(2, 4, -5))