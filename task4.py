class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на{direction}')

    def show_speed(self):
        print(f'Машина {self.name} - текущая скорость {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        is_police = False
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} - cкорость превышена')
        else:
            super().show_speed()

class SportCar(Car):
    def __init__(self, speed, name):
        is_police = False
        color = 'red'
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, name):
        is_police = False
        super().__init__(speed, 'black', name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} - cкорость превышена')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed):
        name = 'Police'
        is_police = True
        color = 'blue'
        super().__init__(speed, color, name, is_police)

t1 = TownCar(30,'green','AE256')
t2 = TownCar(70,'yellow','KJ438')
s = SportCar(100, 'Ferrari 12')
w = WorkCar(40,'KL946')
p = PoliceCar(64)
print('Машина ',t1.name,' Цвет ', t1.color)
t1.show_speed()
print(f'Машина {t2.name}, полиция - {t2.is_police}')
t2.show_speed()
print(s.name)
s.show_speed()
w.go()
w.show_speed()
p.turn('право')
t2.stop()

