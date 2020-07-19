def division (var_1, var_2):
    if var_2 == 0:
        return 'Деление на 0 невозможно'
    else:
        return round(var_1/var_2, 2)

def my_func (var_1, var_2, var_3):
    return sum([var_1, var_2, var_3]) - min([var_1, var_2, var_3])

def my_func_2(var_1, var_2):
    print (var_1**var_2)

def my_func_2_1(var_1, var_2):
    result = 1
    for i in range(abs(var_2)):
        result = result / var_1
    return round(result, 4)

# num_1 = int(input('Введите число 1 '))
# num_2 = int(input('Введите число 2 '))
# num_3 = int(input('Введите число 3 '))
# print(division(num_1, num_2))
# print(my_func(num_1, num_2, num_3))
# my_func_2(4, -6)
# print(my_func_2_1(4, -6))

# именованные параметры
def second_func(name, surname, year_birth, city, email, phone_number):
    print(f"имя - {name}\nфамилия - {surname}\nгод рождения - {year_birth}\nгород - {city}\nemail - {email}\nтелефон - {phone_number}")


second_func(name = 'Ksenia', surname='Epshteyn', year_birth='1988', city = 'Moscow', email = 'ksuxampei@yandex.ru', phone_number = '+79671130186')
