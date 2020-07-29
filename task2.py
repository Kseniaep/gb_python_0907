class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, m=25, th=5):
        return self._length * self._width * m * th

r = Road(20, 5000)
r_mass = round(r.mass()/1000,1)
print(f'Вес необходимого покрытия {r_mass} т')