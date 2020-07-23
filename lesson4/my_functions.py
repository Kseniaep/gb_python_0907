from itertools import count, cycle

def generator_1(number):
    for el in count(number):
        if el > number + 9:
            """Выводит 10 чисел, начиная с заданного"""
            break
        else:
            print(el)

def generator_2(my_list):
    iter = cycle(my_list)
    c = 0
    while c < 5:
        """Выводит 5 значений по циклу"""
        print(next(iter))
        c += 1