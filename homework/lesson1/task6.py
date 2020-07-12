a = int(input("Введите результат первого дня в км: "))
b = int(input("Введите целевой результат в км: "))
count = 1
print("Результаты:")
print(f"{count}-й день - {a} км")
while a < b:
    a = round(a * 1.1, 2)
    count += 1
    print(f"{count}-й день - {a} км")
print(f"Ответ: На {count}-й день спортсмен достиг результата {b} км")