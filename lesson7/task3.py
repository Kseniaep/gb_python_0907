class Cell:

    def __init__(self, cell):
        self.cell = cell

    @property
    def cell(self):
        return self.__cell

    @cell.setter
    def cell(self, cell):
        if cell <= 0:
            self.__cell = 1
        else:
            self.__cell = int(cell)

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return 'Операцию вычитания провести невозможно'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        return self.cell // other.cell

    def make_order(self, num):
        str = ''
        for i in range(1, self.cell + 1):
            str += '*'
            if (i % num == 0) or (i == self.cell):
                str +='\n'
        return str

cl_1 = Cell(10)
cl_2 = Cell(4)
print(cl_1 + cl_2)
print(cl_1 - cl_2)
print(cl_2 - cl_1)
print(cl_1 * cl_2)
print(cl_1 / cl_2)
print(cl_1.make_order(3))
print(cl_2.make_order(2))
cl_3 = Cell(0)
cl_4 = Cell(5.7)
cl_5 = Cell(-3)
print(cl_3.make_order(3))
print(cl_4.make_order(4))
print(cl_5.make_order(2))