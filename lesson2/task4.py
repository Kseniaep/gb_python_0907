str = input('Введите строку ')
list = str.split( )
count = 1
for i in list:
    print(f'{count}.{i[:10]}')
    count += 1