def sep(sep, sep2):
    return sep * sep2


#Задание 1.
from time import sleep
class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(2)
            if i == 3:
                sleep(7)
            i += 1

run = TrafficLight()
run.running()

print(sep('*', 50))

#Задание 2.
class Road:
    def __init__(self, length, width, volume, mas):
        self._length = length
        self._width = width
        self.volume = volume
        self.mas = mas

    def mass(self):
        return self._length * self._width * self.volume * self.mas

res = Road(20, 5000, 5, 25)
print(f'Масса в тоннах будет равна: {res.mass()/1000}')

print(sep('*', 50))

#Задание 3 .
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + '' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position("Алексей ", "Черноусов", "Тренер", 30000, 15000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

print(sep('*', 50))

#Задание 4.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn_right(self):
        print(f'{self.name} повернула направо.')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость для авто {self.name} равна {self.speed}')

        if self.speed > 40 :
            return f'Скорость {self.name} выше разрешенной для вашего авто.'
        else:
            return f'Скорость для {self.name} разрешена.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость для авто {self.name} равна {self.speed}')

        if self.speed > 60 :
            return f'Скорость {self.name} выше разрешенной для вашего авто.'
        else:
            return f'Скорость для {self.name} разрешена.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина.'
        else:
            return f'{self.name} не полицейская машина.'

bmw = SportCar(120, 'Белая', 'БМВ', False)
lada = PoliceCar(60, 'Синяя', 'Лада', True)
reno = TownCar(50, 'Черная', 'Рено', False)
kamaz = WorkCar(50, 'Оранжевый', 'Камаз', False)

print(f'Ваша БМВ {bmw.color}')
print(bmw.go(), bmw.show_speed(), bmw.turn_right())
print(f'Машина {lada.name} полицейская? {lada.is_police}')
print(f'{kamaz.show_speed()}')

print(sep('*', 50))

#Задание 5.
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У вас сейчас {self.title}. Запуск отрисовки ручкой.')

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У вас сейчас {self.title}. Запуск отрисовки карандашом.')

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'У вас сейчас {self.title}. Запуск отрисовки маркером.')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())