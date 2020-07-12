rev = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
gain = rev - cost
if gain > 0:
    print ("Фирма отработала с прибылью")
    print ("Рентабельность %.2f" % (rev/cost))
    num_emp = int(input("Введите численность сотрудников: "))
    gain_emp = round(gain / num_emp, 2)
    print (f"Прибыль на одного сотрудника {gain_emp} руб.")
elif gain == 0:
    print("Фирма отработала в ноль")
else:
    print("Фирма отработала с убытком")
