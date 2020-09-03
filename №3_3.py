def my_func(a=0, b=0, c=0):
    my_list = [a, b, c]
    sum_list = []
    first_number = max(my_list)
    my_list.remove(first_number)
    sum_list.append(first_number)
    second_number = max(my_list)
    return first_number + second_number


print(my_func(100, 12, -300))
