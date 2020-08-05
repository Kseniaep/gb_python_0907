import re

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

new_list = []
inp_data = ''
while inp_data != 'stop':
    inp_data = input("Введите положительное число: ")
    try:
        if re.match(r"[a-z]+",inp_data):
            raise OwnError("Вы ввели текст!")
    # except ValueError:
    #     print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        new_list.append(int(inp_data))
print(new_list)