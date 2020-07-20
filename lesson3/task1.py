def division (var_1, var_2):
    if var_2 == 0:
        return 'Деление на 0 невозможно'
    else:
        return round(var_1/var_2, 2)

num_1 = int(input('Введите число 1 '))
num_2 = int(input('Введите число 2 '))
print(division(num_1, num_2))