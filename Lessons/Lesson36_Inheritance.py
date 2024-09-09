class Animal:
    alive = True
    def eat(self):
        print('This animal is eating.')
    def sleep(self):
        print('This animal is sleeping.')
class cat(Animal):
     def walk(self):
         print('This cat can walk.')

class rabbit(Animal):
   def run(self):
       print('This rabbit can run.')

class fish(Animal):
    def swim(self):
        print('This fish can swim.')


cat1 = cat()
rabbit1 = rabbit()
fish1 = fish()

fish1.eat()
rabbit1.eat()

print(fish1.alive)
cat1.walk()
rabbit1.run()