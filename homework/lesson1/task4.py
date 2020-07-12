num = int(input("Введите целое положительное число: "))
max = 0
while num > 0:
    dig = num % 10
    if dig > max:
        max = dig
    num = num // 10
print ("Максимальная цифра ", max)