# str.format = optional method that give user more control when displaying output

animal = 'cow'
item = 'moon'

print('The {} jumped over the {}'.format(animal,item))
print('The {1} jumped over the {1}'.format(animal,item)) # positional argument

# keyword argument
print('The {animal} jumped over the {item}'.format(animal='dog',item='fence'))

text = 'the {} jumped over the {}'
print(text.format(animal,item))

# add padding to a name
name = 'luffy'

print('Hello {:10}.Nice to meet you.'.format(name))
print('Hello {name:<10}.Nice to meet you.'.format(name='zoro'))
print('Hello {:>10}.Nice to meet you.'.format(name))
print('Hello {:^10}.Nice to meet you.'.format(name))


number = 3.14159

print('The number pi is {:.3f}'.format(number))
print('The number is {:,}'.format(100000))
print('The number is {:o}'.format(100000))
print('The number is {:x}'.format(100000))
print('The number is {:e}'.format(100000)) # scientific 
print('The number is {:b}'.format(69))
