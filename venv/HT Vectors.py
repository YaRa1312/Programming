import math

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

#додавання (перевірка)
    def add(self, other):
        print("(" + str(self.x + other.x) + ", " + str(self.y + other.y) + ", " + str(self.z + other.z) + ")")
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

#1) векторний добуток
    def mul(self, other):
        print("("+str((self.y*other.z)-(self.z*other.y))+"), ("+str((self.x*other.z)-(self.z*other.x))+"), ("+str(+(self.x*other.y)-(self.y*other.x)+")"))
    def __mul__(self, other):
        return Vector((self.y*other.z)-(self.z*other.y), (self.x*other.z)-(self.z*other.x), +(self.x*other.y)-(self.y*other.x))
    def __str__(self):
       #return "("+str((self.y * other.z)-(self.z * other.y))+", "+str(-(self.x * other.z)-(self.z * other.x))+", "+str(+(self.x * other.y)-(self.y * other.x))+")"
        return "("+str(self.x)+", "+str(-self.y)+", "+str(self.z)+")"

#2) модуль вектора
    #def my_func(self, other):
    #    print("("+str(self.x*self.x)+")"+"("+str(self.y+self.y)+")"+"("+str(self.z*self.z)+")")
    #def __my_func__(self, other):
    #    return Vector("("+str(self.x*self.x)+")"+"("+str(self.y+self.y)+")"+"("+str(self.z*self.z)+")")
    #def __str__(self):
    #    return "("+str(self.x*self.x)+")"+"("+str(self.y+self.y)+")"+"("+str(self.z*self.z)+")"
#print(my_func)

#3) протилежний вектор
#4) порівняння векторів за довжиною
#5) чи вектори колінеярні?

a = Vector(1, 2, 3)
#видає квадрати x, y, z
#print(a)

b = Vector(10, 9, 8)
#видає квадрати x, y, z
#print(b)
#print(a+b)
print(a*b)
#print(my_func)