def division(first_number, second_number):
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        print('Деление на 0')
    else:
        return result


user_first = int(input('Введите делимое: '))
user_second = int(input('Введите делитель: '))
print((division(user_first, user_second)))
