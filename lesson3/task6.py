def int_func(str):
    return str.title()

def up_str(str):
    list = str.split()
    for i in range(len(list)):
        list[i] = int_func(list[i])
    return list

inp_str = input('Введите строку ')
print (' '.join(up_str(inp_str)))