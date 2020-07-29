import time

class TrafficLight:

    def __init__(self):
        self.__color = 'красный'

    def running(self):
        print(f"Светофор запущен")
        while True:
            print(f"Цвет светофора - {self.__color}")
            time.sleep(7)
            self.__color = 'желтый'
            print(f"Цвет светофора - {self.__color}")
            time.sleep(5)
            self.__color = 'зеленый'
            print(f"Цвет светофора - {self.__color}")
            time.sleep(3)
            self.__color = 'красный'

tl = TrafficLight()
tl.running()