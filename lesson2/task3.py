autumn = [9, 10, 11]
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]

month = int(input('Введите номер месяца от 1 до 12 '))
if (month < 1) or (month > 12):
    print('Значение введено неверно')
elif month in autumn:
    print('Осень')
elif month in winter:
    print('Зима')
elif month in spring:
    print('Весна')
elif month in summer:
    print('Лето')

period = dict(autumn = [9,10,11], winter=[1,2,12], spring = [3,4,5], summer = [6,7,8])
month = int(input('Введите номер месяца от 1 до 12 '))
if (month < 1) or (month > 12):
    print('Значение введено неверно')
else:
    for key, value in period.items():
        if month in value:
            print(key)
