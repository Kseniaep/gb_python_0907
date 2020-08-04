class MyDate:
    @staticmethod
    def date_num(date_str):  # Статический метод
        new_list = list(map(int, date_str.split('-')))
        return new_list

    @classmethod
    def my_method(cls, param):  # Метод класса
        new_list = MyDate.date_num(param)
        if new_list[0] == 0 or new_list[0] > 31:
            print('День задан неверно')
        if new_list[1] == 0 or new_list[1] > 12:
            print('Месяц задан неверно')
        if new_list[2] > 2020:
            print('Дата задана в будущем')


my_date = input(f'Введите дату\n')
md = MyDate()
md.my_method(my_date)  # Вызов метода класса через экземпляр