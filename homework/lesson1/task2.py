
time = int(input("Введите время в секундах: "))
time_hour = time // 3600
time_min = (time % 3600) // 60
time_sec = (time % 3600) % 60
print("{:02d}:{:02d}:{:02d}".format(time_hour, time_min, time_sec))
