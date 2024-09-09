from car import Car as c

car1 = c('Porsche','911',2021,'Blue')
car2 = c('Ford','Mustang',2019,'Black')

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

c.wheels = 5
car1.wheels = 2

print(car1.wheels)
print(car2.wheels)

car1.drive()
car2.drive()
