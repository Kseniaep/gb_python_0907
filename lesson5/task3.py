with open("salary.txt") as f_obj:
    count = 0
    sum = 0
    for line in f_obj:
        list = line.split()
        count += 1
        sum += float(list[1])
        if float(list[1])>=20:
            print(line)
    print(f'Средняя зарплата {round(sum/count,2)} тыс.руб')