from itertools import cycle
from sys import argv

script_name, my_list = argv
iter = cycle(my_list)
c = 0
while c < 5:
    """Выводит 5 значений по циклу"""
    print(next(iter))
    c += 1