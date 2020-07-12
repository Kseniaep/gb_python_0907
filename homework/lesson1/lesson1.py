name = input("Введите Ваше имя: ")
print ("Вас зовут ", name)
num = int(input("Введите целое число: "))
print ("Вы ввели число ", num)
print ("Квадрат этого числа ", num ** 2)

time = int(input("Введите время в секундах: "))
time_hour = time // 3600
time_min = (time % 3600) // 60
time_sec = (time % 3600) % 60
print("{:>2}:{:>2}:{:>2}".format('time_hour', 'time_min, 'time_sec'))
