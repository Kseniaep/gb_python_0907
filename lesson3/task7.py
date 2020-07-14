def division (var_1, var_2):
    if var_2 == 0:
        return 'Деление на 0 невозможно'
    else:
        return round(var_1/var_2, 2)

def my_func (var_1, var_2, var_3):
    return sum([var_1, var_2, var_3]) - min([var_1, var_2, var_3])

num_1 = int(input('Введите число 1 '))
num_2 = int(input('Введите число 2 '))
num_3 = int(input('Введите число 3 '))
print(division(num_1, num_2))
print(my_func(num_1, num_2, num_3))

# именованные параметры
def second_func(var_2, var_1, var_3):
    print(f"var_2 - {var_2}; var_1 - {var_1}; var_3 - {var_3}")


second_func(var_1=10, var_2=20, var_3=30)