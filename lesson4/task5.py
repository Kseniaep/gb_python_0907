from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

new_list = [el for el in range(10, 1001) if el % 2 == 0]
# print(new_list)
print(reduce(my_func, new_list))
