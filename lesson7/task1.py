class Matrix:

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        l = len(data[0])
        for el in data[1:]:
            if len(el) != l:
                raise ValueError('Количество элементов во всех строках должно совпадать')
        self.__data = data
        self.__dimension = (len(data), l)

    def __str__(self):
        new_str = ''
        for el in self.data:
            new_str = new_str + ' '.join(map(str,el)) + '\n'
        return new_str

    def __add__(self, other):
        if self.__dimension != other.__dimension:
            return 'Сложение матриц разной размерности невозможно'
        new_list = []
        x,y = self.__dimension
        for el in range(x):
            str_list = []
            for i in range(y):
                str_list.append(self.data[el][i]+other.data[el][i])
            new_list.append(str_list)
        return Matrix(new_list)

m1 = Matrix([[1,2,3],[4,5,6]])
m3 = Matrix([[7,8,9,10],[1,2,3,5]])
m4 = Matrix([[7,8,9],[1,2,3]])
print(m1)
print(m3)
print(m1+m3)
print(m1)
print(m4)
print(m1+m4)
m2 = Matrix([[7,8,9,10],[1,2,3]])
