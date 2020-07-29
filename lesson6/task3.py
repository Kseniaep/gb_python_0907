class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict()
        self._income['wage'] = wage
        self._income['bonus'] = bonus

class Position(Worker):
    def __init__(self, name, surname,position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Сотрудник {self.surname} {self.name}')

    def get_total_income(self):
        inc = self._income['wage'] + self._income['bonus']
        print(f'Зарплата {inc}')

p = Position('Иван','Иванов','менеджер',100,50)
print(p.name)
print(p.surname)
print(p.position)
print(p._income)
p.get_full_name()
p.get_total_income()