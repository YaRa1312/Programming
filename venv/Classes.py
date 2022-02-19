class Animal:
    def __init__(self):
        self.can_run = False
        self.can_fly = False


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Eagle(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Pegasus(Horse, Eagle):
    pass


a = Animal()
print("Animal can run", a.can_run)
print("Animal can fly", a.can_fly)
h = Horse()
print("Horse can run", h.can_run)
print("Horse can fly", h.can_fly)
e = Eagle()
print("Eagle can run", e.can_run)
print("Eagle can fly", e.can_fly)
p = Pegasus()
print("Pegasus can run", p.can_run)
print("Pegasus can fly", p.can_fly)

#class Bird():
#    def __init__(self, given_color, given_will_eat_me, given_feather):
#        self.color = given_color
#        self.will_eat_me = given_will_eat_me
#        self.feather = given_feather
    #def __init__(self, can_fly):
    #    self.can_fly = can_fly
    #def eat(self):
    #    pass
    #def move(self):
    #    print("I can fly!")
    #def sing(self):
    #    pass

#class Parrot(Bird):
#    def __init__(self, given_color, given_will_eat_me, given_feather, given_can_speak):
#        super().__init__(given_color, given_will_eat_me, given_feather)
        #self.color = given_color
        #self.will_eat_me = given_will_eat_me
        #self.feather = given_feather
#        self.can_speak = given_can_speak

#kesha = Parrot ('blue', True, True, False)
#print(kesha.color)

#class Penguin(Bird):
#    feather = False
#    def move(self):
        #print("I can dance!")

#class Stra(Parrot, Penguin):
#    pass

#andrii = Stra(False)
#print(andrii.can_fly)
#print(andrii.can_speak)
#print(andrii.feather)

#bird = Bird(True)
#(bird.can_fly)
#bird.color = 'white'
#print(bird.color)

#kesha = Parrot(True)
#print(kesha.can_speak)

#happy = Penguin(False)
#happy.move()