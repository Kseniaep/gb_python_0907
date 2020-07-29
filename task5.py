class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        title = 'pen'
        super().__init__(title)

    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def __init__(self):
        title = 'pencil'
        super().__init__(title)

    def draw(self):
        print('Карандаш')

class Handle(Stationery):
    def __init__(self):
        title = 'handle'
        super().__init__(title)

    def draw(self):
        print('Маркер')

s = Stationery('brusch')
print(s.title)
s.draw()
p = Pen()
print(p.title)
p.draw()
pl = Pencil()
print(pl.title)
pl.draw()
h = Handle()
print(h.title)
h.draw()