from itertools import count
from sys import argv

script_name, number = argv
for el in count(number):
    if el > number + 10:
        """Выводит 10 чисел, начиная с заданного"""
        break
    else:
        print(el)