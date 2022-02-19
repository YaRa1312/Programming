#15.03.2021
#a = 8
#def my_func (a, b):
#    a += 1
#    return a * 3 + b * 2

#print(my_func(a, 3))
#print(a)

#class Cat():
#    def __init__(self, weight):
#        self.weight = weight

#cat = Cat(5)
#print(cat.weight)
#cat.weight = -5
#print(cat.weight)


#29.03.2021
#from abc import ABC, abstractmethod
#class Bird(ABC):
#    @abstractmethod
#    def move(self):
#        print("I can move!")

 #   @abstractmethod
#    def speak():
#        pass

#class Parrot (Bird):
#    def move(self):
#        pass
#        print("I can fly!")

#kesha = Parrot()
#kesha.move()
#bird = Bird()

#class Vector():
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def add(self, b):
#        print("("+str(self.x+b.x)+", "+str(self.y+b.y)+")")

#    def __add__(self, b):
#        return Vector (self.x+b.x, self.y+b.y)
#    def __str__(self):
#        return "("+str(self.x)+", "+str(self.y)+")"

#    def __mul__(self, other):
#        return self.x*other.x + self.y*other.y

#a = Vector(1, 2) #self = a, x = 1, y = 2
#print(a)
#b = Vector(2, 1)
#print(b)
#print(a+b)
#a.add(b)
#a + b
#a.__add__(b)
#print(type(a*b))

#from abc import ABC, abstractmethod


#class Bird(ABC):
#    @abstractmethod
#    def move(self):
#        print("I can move!")

#    @abstractmethod
#    def speak():
#        pass


#class Parrot(Bird):
#    def move(self):
        # print("I can fly!")
#        pass


#kesha = Parrot()
#kesha.move()
# bird = Bird()


#______________


class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        print("(" + str(self.x + b.x) + ", " + str(self.y + b.y) + ", " + str(self.z + b.z) + ")")

    def __add__(self, other):
        #    c = Vector(self.x+b.x, self.y+b.y)
        return Vector(self.x + b.x, self.y + b.y, self.z + b.z)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) +")"

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    #def mul(self, other):
    #    return Vector(((self.y * other.z) - (self.z * other.y)) - ((self.x * other.z) - (self.z * other.x)) - ((self.x * other.y) - (self.y * other.x)))
        #return (self.y * other.z - self.z * other.y)


a = Vector(1, 2, 3)
print(a)
b = Vector(2, 1, 3)
print(b)
#print(a+b)
print(a*b)

def cross(a, b):
    c = [a[y]*b[z] - a[z]*b[y],
         a[z]*b[x] - a[x]*b[z],
         a[x]*b[y] - a[y]*b[x]]
    return c
print(cross(a, b))

#print(type(a * b))