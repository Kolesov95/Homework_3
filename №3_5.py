new_list = []
new_q_list = []
my_sum = 0
while True:
    user_request = input('Введите числа через пробелы или q для выхода: ')
    my_list = user_request.split()
    if 'q' in my_list:
        q_number = my_list.index('q')
        for i in my_list[:q_number]:
            new_q_list.append(int(i))
        my_sum = my_sum + sum(new_q_list)
        print(my_sum)
        break
    else:
        for i in my_list:
            new_list.append(int(i))
        my_sum = my_sum + sum(new_list)
        new_list = []
        print(my_sum)

