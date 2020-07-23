from sys import argv

script_name, work, rate, bonus = argv

salary = (work * rate) + bonus
print("Зарплата: ", salary)