def int_func(request):
    result = request.capitalize()
    return result


user_request = input('Введите слова: ')
new_map = map(int_func, user_request.split())
print(' '.join(new_map))
