list_2 = []
n = int(input('Введите количество элементов в списке - целое число '))
for i in range(n):
    new_element = input(f'Введите {i+1}-й элемент\n')
    list_2.append(new_element)
print(list_2)
for i in range(1,n,2):
    list_2[i], list_2[i-1] = list_2[i-1], list_2[i]
print(list_2)