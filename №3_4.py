def my_func(x, y):
    degree = 1
    result = 1/x
    while degree < abs(y):
        result = result * (1/x)
        degree += 1
    return result


print(my_func(12, -3))

