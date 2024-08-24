# 19

try:
    with open('C:\\Users\\user\\Desktop\\Resources\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('This file is not found')

