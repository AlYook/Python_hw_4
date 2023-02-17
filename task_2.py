"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def render_user_info(first_name, last_name, birthday, city, email, phone):
    print(f'{first_name} {last_name} {birthday} года рождения, проживает в городе {city} email: {email}, телефон: {phone}')


first_name = input('Введите имя:')
last_name = input('Введите фамилию:')
birthday = input('Введите год рождения:')
city = input('Введите город:')
email = input('Введите email:')
phone = input('Введите номер телефона:')


render_user_info(
    birthday=birthday,
    first_name=first_name,
    last_name=last_name,
    email=email,
    phone=phone,
    city=city
)
