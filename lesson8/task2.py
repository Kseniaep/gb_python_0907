def division(a, b):
    try:
        res = float(a) / float(b)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Что-то пошло не так")
    else:
        print(f"Все хорошо. Результат - {res}")
    finally:
        print("Программа завершена")

num_1 = input(f'Введите делимое\n')
num_2 = input(f'Введите делитель\n')
division (num_1, num_2)
