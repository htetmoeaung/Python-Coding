# *args = parameter that will pack all the arguments into a tuple
#         useful so that a function can a accept a varying amount of arguments


def add(*args):
    sum = 0
    stuff = list(args)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum


print(add(1,2,3,4,5))