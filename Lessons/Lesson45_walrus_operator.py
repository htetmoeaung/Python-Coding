# walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assign values to variables as part of a larger expression

# foods = list()
# while True:
#     food = input("What food do you like? ")
#     if food == 'quit':
#         print(foods)
#         break
#     foods.append(food)

foods = list()

while food := input('What food do you like? ') != 'quit':
    foods.append(food)