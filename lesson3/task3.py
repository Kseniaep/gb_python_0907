def my_func (var_1, var_2, var_3):
    return sum([var_1, var_2, var_3]) - min([var_1, var_2, var_3])

num_1 = int(input('Введите число 1 '))
num_2 = int(input('Введите число 2 '))
num_3 = int(input('Введите число 3 '))
print(my_func(num_1, num_2, num_3))