from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def expens(self):
        pass

class Coat(Clothes):

    def __init__(self,v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 38 or v > 56:
            raise ValueError('Заданное значение вне диапазона')
        else:
            self.__v = v

    def expens(self):
        return (round(self.v/6.5,1) + 0.5)


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self,h):
        if h < 1 or h > 2:
            raise ValueError('Заданное значение вне диапазона')
        else:
            self.__h = h

    def expens(self):
        return round(2*self.h,1) + 0.3


s = Suit(1.52)
c = Coat(44)

print(s.expens())
print(c.expens())

s = Suit(2.2)