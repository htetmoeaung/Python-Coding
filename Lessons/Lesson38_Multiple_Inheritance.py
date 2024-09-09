# Multiple Inheritance = when a child class is derived from more than one parent class

class Prey:
    def flees(self):
        print('this animal flees')

class Predator:
    def hunts(self):
        print('this animal hunts')

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flees()
hawk.hunts()
fish.flees()
fish.hunts()