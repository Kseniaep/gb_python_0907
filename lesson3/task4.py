def my_func(var_1, var_2):
    print (var_1**var_2)

def my_func_1(var_1, var_2):
    result = 1
    for i in range(abs(var_2)):
        result = result / var_1
    return result

my_func(4, -6)
print(my_func_1(4, -6))