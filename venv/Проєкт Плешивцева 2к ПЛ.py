from abc import ABC, abstractmethod
class Human(ABC):
    can_speak = True
    def __init__(self, age, eyes, zodiac_sign):
        self.__age = age                                #інкапсуляція: приватна змінна (private)
        self._eyes = eyes                               #інкапсуляція: захищена змінна (protected)
        self.zodiac_sign = zodiac_sign                  #публічна змінна (public)

    @abstractmethod
    def __str__(self):                                  #магічний метод (MM)
        pass
    def action(self):                                   #instance method (IM)
        pass                                            #P.S. Реалізацію ММ та ІМ можна побачити в кожному об'єкті проєкту

    def set_age(self, age):                             #setter
        if age in range(0, 76):                         #у кожному об'єкті перевіряє вік на реалістичність
            self.__age = age                            #працює, якщо в інформації про об'єкт і в рядочку із set_age
        else:                                           #ОДНАКОВА цифра
            print("You see, the age is unreal.")

    def get_age(self, age):                             #getter
        return self.__age


class Man(Human):                                       #успадкування
    has_moustache = True
    usually_has_long_hair = False
    is_already_18_yo = True
    likes_mushrooms = True
    def __init__(self, age, eyes, zodiac_sign):
        self.__age = age
        self._eyes = eyes
        self.zodiac_sign = zodiac_sign
    def __str__(self):
        return "Karpo: " '{}, {}, {}'.format(self.__age, self._eyes, self.zodiac_sign)
    def action(self):
        print("Karpo repairs carts.")
    pass

karpo = Man(22, "brown", "Aries")
print(karpo)
karpo.set_age(22)
print("Karpo has moustache", karpo.has_moustache)
print("Karpo has long hair", karpo.usually_has_long_hair)
print("Karpo is already 18 years old", karpo.is_already_18_yo)
print("Karpo likes mushrooms", karpo.likes_mushrooms)
karpo.action()


class Woman(Human):                                     #успадкування
    has_moustache = False
    usually_has_long_hair = True
    is_already_18_yo = True
    likes_mushrooms = False
    def __init__(self, age, eyes, zodiac_sign):
        self.__age = age
        self._eyes = eyes
        self.zodiac_sign = zodiac_sign
    def __str__(self):
        return "Motrya: " '{}, {}, {}'.format(self.__age, self._eyes, self.zodiac_sign)
    def action(self):
        print("Motrya embroiders shirts.")

motrya = Woman(21, "green", "Virgo")
print(motrya)
motrya.set_age(21)
print("Motrya has moustache", motrya.has_moustache)
print("Motrya has long hair", motrya.usually_has_long_hair)
print("Motrya is already 18 years old", motrya.is_already_18_yo)
print("Motrya likes mushrooms", motrya.likes_mushrooms)
motrya.action()


class Boy(Man, Woman):                              #поліморфізм
    has_moustache = False
    usually_has_long_hair = False
    is_already_18_yo = False
    likes_mushrooms = False
    def __init__(self, age, eyes, zodiac_sign):
        self.__age = age
        self._eyes = eyes
        self.zodiac_sign = zodiac_sign
    def __str__(self):
        return "Ivan: " '{}, {}, {}'.format(self.__age, self._eyes, self.zodiac_sign)
    def action(self):
        print("Ivan plays.")

ivan = Boy(3, "green", "Sagittarius")
print(ivan)
ivan.set_age(3)
print("Ivan has moustache", ivan.has_moustache)
print("Ivan has long hair", ivan.usually_has_long_hair)
print("Ivan is already 18 years old", ivan.is_already_18_yo)
print("Ivan likes mushrooms", ivan.likes_mushrooms)
ivan.action()


class Girl(Man, Woman):                              #поліморфізм
    has_moustache = False
    usually_has_long_hair = True
    is_already_18_yo = False
    likes_mushrooms = True
    def __init__(self, age, eyes, zodiac_sign):
        self.__age = age
        self._eyes = eyes
        self.zodiac_sign = zodiac_sign
    def __str__(self):
        return "Stephaniya: " '{}, {}, {}'.format(self.__age, self._eyes, self.zodiac_sign)
    def action(self):
        print("Stephaniya dances.")

stephaniya = Girl(4, "brown", "Capricornus")
print(stephaniya)
motrya.set_age(4)
print("Stephaniya has moustache", stephaniya.has_moustache)
print("Stephaniya has long hair", stephaniya.usually_has_long_hair)
print("Stephaniya is already 18 years old", stephaniya.is_already_18_yo)
print("Stephaniya likes mushrooms", stephaniya.likes_mushrooms)
stephaniya.action()


class Horse:
    TOTAL_HORSES = 0
    def __init__(self):
        Horse.TOTAL_HORSES = Horse.TOTAL_HORSES+1
    @classmethod                                                    #classmethod
    def total_horses(cls):
        print("Total horses:", cls.TOTAL_HORSES)

    def decorator_with_arguments(function):                                                                     #Мій декоратор, який приймає аргументи
        def wrapper_accepting_arguments(arg1, arg2, arg3, arg4):                                                #("horses", "cows", "pigs", "hens").
            print("Their animals are {0}, {1}, {2} and {3}.".format(arg1, arg2, arg3, arg4))                    #Для цього він передає їх до wrapper_function
            function(arg1, arg2, arg3, arg4)                                                                    #Далі аргументи передаються до
        return wrapper_accepting_arguments                                                                      #"задекорованої" функції,
    @decorator_with_arguments                                                                                   #тобто до animals
    def animals(animal_one, animal_two, animal_three, animal_four):
        print("They have {0}, {1}, {2} and {3}.".format(animal_one, animal_two, animal_three, animal_four))
    animals("horses", "cows", "pigs", "hens")

horse1 = Horse()                                                    #реалізація classmethod
horse2 = Horse()
horse3 = Horse()
Horse.total_horses()


import math
class Field():
    def __init__(self, length, width, crop):
        self.length = length
        self.width = width
        self.crop = crop
    @staticmethod                                                   #staticmethod
    def area(length, width):
        return length * width
field = Field(45, 67, "wheat")
print(f"The area of the field is {field.area(45, 67)} ha.")


class Cock:                                                                 #Шаблон Proxy. Півень будить людей.
    def waking_up(self) -> None:                                            #А будильник є Proxy відносно півня.
        pass                                                                #Вони мають загальний інтерфейс (обидва
class AlarmClock:                                                           #виконують однакову функцію waking_up).
    def __init__(self) -> None:
        self._klass = Cock()
    def waking_up(self) -> None:
        print(f"Waking up the whole world thanks to {self._klass}.")
alarm_clock = AlarmClock()
alarm_clock.waking_up()
alarm_clock = compile('print("They use an alarm clock.")', 'test', 'eval')
exec(alarm_clock)


import unittest                                                             #unittest
class ThisTestCase(unittest.TestCase):                                      #пропускає класи,
    @unittest.skip("showing class skipping")                                #які йдуть після нього
    class ThisSkippedTestCase(unittest.TestCase):                           #і не відповідають
        def test_not_runs(self):                                            #змісту повісті
            pass
if __name__ == "__main__":
    unittest.main()


class Bird:                                                                     #перевірка роботи unittesting
    can_fly = True
    def __init__(self, name, feather_color):
        self.__name = name
        self._feather_color = feather_color
    def intro(self):
        return "Bird1: " '{}, {}'.format(self.__name, self._feather_color)
bird1 = Bird("Kesha", "red")
print(bird1)
print("Kesha can fly", bird1.can_fly)
