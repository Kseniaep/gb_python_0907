def adder (str):
    list = str.split()
    sum = 0
    n = True
    for i in list:
        if i.isdigit():
            sum += int(i)
        elif i == 's':
            n = False
            break
    return sum, n

print('Введите последовательность')
checker = True
global_sum = 0
while checker:
    inp_str =input()
    sum_str, checker = adder(inp_str)
    global_sum += sum_str
    print (global_sum)