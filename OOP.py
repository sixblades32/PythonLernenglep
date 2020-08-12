class Character():
    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


class Car():
    DEAD_STATUS = 0  # константы пишем капс локом

    def __init__(self, speed=100, hp=300, status=100):  # иницилируем значения жлемента класса при назначении класса
        self.speed = speed
        self._hp = hp  # защищенный атрибут - нельзя использ из вне, но можно наследниками
        self.__status = status  # приватный атрибут - нельзя использ не из вне, не из наследников, а только внутри класса объявления, не получится c.status, но можно все таки изменить c._Character__status = 'dead'

    def notfall(self, damage):
        self.speed -= damage * 0.25
        self._hp -= 100

    # чтобы установить защищенному атрибуту значение через простое свойство:
    class BankAccount:

        def __init__(self, name, balance):
            self.name = name
            self.__balance = balance  # защищенный атрибут

        def get_balance(
                self):  # функция посрдеством которой можно обратиться к защищенному атрибуту и узнать его значение
            return self.__balance

        def set_balance(self, value):  # функция позволяющая изменить значение защищенного атрибута из вне
            self.__balance == value

        def delete_balance(self):
            del self.__balance

        balance = property(fget=get_balance, fset=set_balance,
                           fdel=delete_balance)  # посредством проперти создали уже не функцию, а свойство для изменения и получения баланса
        # d.balance возвращает значение
        # d.balance = 777 изменяет
        # del d.balance атрибут класса не будет иметь значения balance

        mybalance = property()
        mybalance = mybalance.setter(set_balance)
        mybalance = mybalance.getter(get_balance)
        mybalance = mybalance.deleter(delete_balance)

    @property  # для чтения защищенного атрибута из вне,
    def hp(self):
        return self._hp

    @hp.setter  # для записи в защищенный атрубут с логикой
    def hp(self, hp):
        if hp < 0:
            self._hp = 0
        elif hp > 100:
            self._hp = 100
        else:
            self._hp = hp

    def is_dead(self):
        return self.__status == Car.DEAD_STATUS


unit = Car()

unit.hp = -30

print(unit.hp)


# СТАТИЧЕСКИЕ МЕТОДЫ @staticmethod classmethod

class StaticTest:
    x = 1


t1 = StaticTest()

t1.x = 2

print(
    f'via instance:{t1.x}')  # то есть x через инстанцию и через класс хранится в разных ячейках памяти, в классе не меняется, но меняется у элемента при обращении через t1
print(f'via class:{StaticTest.x}')


# статические методы
class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month}-{self.day}-{self.year}'

    @classmethod
    def millenium_c(cls, month, day):
        return cls(month, day, 2000)  # cls вызывает конструктор init

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)


d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)

print(d1.display())
print(d2.display())


class DateTime(Date):  # наследует класс дейт
    def display(self):
        return f'{self.month}- {self.day}-{self.year} - 00:00:00PM'


dt1 = DateTime(10, 10, 1990)  # конструируется через ДейтТайм

dt2 = DateTime.millenium_s(10, 10)  # конструируется через Date, поэтому не принадлежить классу ДейтТайм

dt3 = DateTime.millenium_c(10,
                           10)  # конструеируется на классе, который вызывает ее поэтому принадлеить классу Дейт Тайм
print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))
print(isinstance(dt3, DateTime))
print(dt1.display())
print(dt2.display())


# В общем данные ститические методы требуются

# Наследование и полиморфизм
class Shape():

    def __init__(self):
        print('Shape created')

    def draw(self):
        raise NotImplementedError("Cant instantiate an abstract class")

    # райзе вводим для того, чтобы в наследниках обязательно надо было переопределять атрибуты, при вызове данных атрибутов будет ошибка
    def area(self):
        raise NotImplementedError("Cant instantiate an abstract class")

    def perimeter(self):
        raise NotImplementedError("Cant instantiate an abstract class")


shape = Shape()


class Rectangle(Shape):  # наследует класс шейп

    def __init__(self, width, height):
        Shape.__init__(
            self)  # в конструкторе класса, который наследует надо передать сначала конструктор от которого наследует

        self.width = width
        self.height = height
        # наследование позволяет использовать функционал родительского класса, а такжее переопределить их
        print('rectangle created')

    def area(self):  # переопределяем функции
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f'Drawing rectangle with width = {self.width} and height = {self.height}')


rect = Rectangle(10, 15)

print(rect.area(), rect.perimeter())

import math


class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        print("Triangle created")

    def draw(self):
        print(f'Drawing triangle with sides - {self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle(10, 10, 10)

triangle.draw()
print(triangle.area(), triangle.perimeter())

for shape in [rect,
              triangle]:  # полиморфизм, из экземпляров разных типов Triangle and Rectangle вызываем методы с одинаковым названием
    shape.draw()
    # Drawing rectangle with width = 10 and height = 15, то есть для  каждого свой результат
    # Drawing triangle with sides - 10, 10, 10


# множественное наследование(дает наследовать больше 1 класса)

# class Animal:
#     def set_health(self, health):
#         print('set in animal')
# class Carnivour(Animal):
#     def set_health(self, health):
#         print("set in carnivour")
# class Mammal(Animal):
#     def set_health(self,health):
#         print("set in mammal")
# class Dog(Mammal,Carnivour):
#     pass #получился так называемый ромб смерти, потому что хищник наследует от анимал и маммал от анимал, а до от них обоих и получается ромб

# dog = Dog()
# dog.set_health(10) #вызывает из маммал из за порядка наследования, то есть если первым написать карнивор Dog(Carnivour, Mammal):

class Animal:
    def set_health(self, health):
        print('set in animal')


class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)
        print("set in carnivour")


class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        print("set in mammal")


class Dog(Mammal, Carnivour):
    def set_health(self, health):
        # Mammal.set_health(self, health) в таком случае вызвает аж до самого родительского класса Animal set in animal, поэтому сет анимал повторяется несколько раз, чтобы этого избежать используем super().set_health(health), поэтому везед вызываем через супер, кроме анимал, изчезает проблема двой инициализации
        # set in mammal
        # set in animal
        # set in carnivour
        # set in dog
        # Carnivour.set_health(self, health)
        super().set_health(health)
        print('set in dog')


# super понадобиться для избежаения повторения инициализации базового класса наследником, он обрабатывает порядком снизу-вверх, слева-направо, то есть сначала самый глубокий animal
dog = Dog()
dog.set_health(10)


class Animal2:
    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage


class Carnivour2(Animal2):
    def __init__(self):
        super().__init__()  # инициальзируем атрибуты базового класса
        self.legs = 4


cat = Carnivour2()
cat.hit(15)
print(cat.health)


# миксины - особенный вид множественного наследования, не создаются как базовый класс

class Vehicle:
    def __init__(self, position):
        self.position = position

    def trevel(self, destination):
        route = calculate_route(source=self.position, to=destination)
        self.move_along(route)

    def calculate_route(self, source, to):
        return 0

    def move_along(self, route):
        print("moving")


class Airplane(Vehicle):
    pass


# поключим радио для машины, но чтобы оно не подключилось к самолете через миксин
class RadioMixin:
    def __init__(self):
        self.radio = Radio()

    def turn_on(self, station):
        self.radio.set_station(station)
        self.radio.play()


class Radio:
    def set_station(self, station):
        self.station = station

    def play(self):
        print(f"Playing {self.station}")


class Car(Vehicle, RadioMixin):
    def __init__(self):
        Vehicle.__init__(self, (10, 20))
        RadioMixin.__init__(self)


car = Car()
car.turn_on("Moscow FM")

# абстрактные классы Абстрактным называется класс, который содержит один и более абстрактных методов. Абстрактным называется объявленный, но не реализованный метод.
from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod  # создаем абстрактную функцию
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        print('calc perimetr')
        # pass

    def drag(self):  # то есть для родительского класса можно одновременно задать и абстракт функ, так и обычные
        print('Basic dragging')


# s = Shape() нельзя так присвоить этот класс будет ошибка
import math


class Triangle(Shape):  # мы наследуем абстрактный класс значит должны переопределить абстракт методы
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f'Drawing triangle with sides ={self.a},{self.b},{self.c}')

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetr(self):
        return self.a + self.b + self.c

    def drag(self):  # так как он был не абстрактным, то его переоределять не обязательнр
        super().draw()
        print('Additionals actions')


t = Triangle(10,10,10)
print(t.perimetr())


#магисеские методы(тандер метод)
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): #переопределяем тандер метод str, который отвечает за строковое представление экземпляра класса при принт
        return f'Point x = {self.x}'

p = Point(3, 4)
print(p)

class Road():
    def __init__(self, length):
        self.lenght = length
    def __len__(self):
        return self.lenght
    def __str__(self):
        return f'A road of length: {self.lenght}'
    def __del__(self):
        return f"A road has been destroyed"