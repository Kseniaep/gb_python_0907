f_obj = open("new_f.txt", 'w')
str = input(f'Введите строку\n')
while str != '':
    f_obj.write(f'{str}\n')
    str = input()
f_obj.close()
