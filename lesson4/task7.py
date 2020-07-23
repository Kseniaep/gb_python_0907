from math import factorial

def fact(n):
    for el in range(n):
        yield factorial(el+1)


n = int(input(f"Введите число\n"))
for el in fact(n):
    print(el)