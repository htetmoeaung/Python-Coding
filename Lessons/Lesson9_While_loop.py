# While Loop = a statement that will execute it's code block,
#              as long as it's condition is true

# name = ''
#
# while len(name) == 0:
#     name = input('Enter your name: ')
#
# print('Hello ',name)

name = None

while not name:
    name = input('Enter your name: ')
print('Hello ',name)
