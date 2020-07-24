my_f = open("new_f.txt", "r")
count = 1
for line in my_f:
    list = line.split()
    print(f'Строка {count},количество слов {len(list)}')
    count += 1
my_f.close()