from sys import argv

script_name, work, rate, bonus = argv

salary = (int(work) * int(rate)) + int(bonus)
print("Зарплата: ",salary)