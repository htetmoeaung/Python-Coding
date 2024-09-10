# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('you drive the car')

    def stop(self):
         print('you stop the car')
class Motorcycle(Vehicle):
    def go(self):
        print('you rides the motorcycle')

    def stop(self):
        print('you stop the motorcycle')

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
