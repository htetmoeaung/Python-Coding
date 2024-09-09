# Method Chaining = calling multiple methods sequentially
#                   each call perform an action on the same object and return self

class Car:
    def start(self):
       print('This car starts the engine')
       return self
    def drive(self):
        print('This car is driving')
        return self
    def brake(self):
        print('This car is using brake')
        return self
    def turn_off(self):
        print('This car turn off the engine')
        return self

car = Car()
# car.start().drive()
# car.brake().turn_off()

(car.start()
 .drive()
 .brake()
 .turn_off()
 )