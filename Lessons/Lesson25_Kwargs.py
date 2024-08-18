# **kwargs = parameter that will pack all arguments into dictionary
#            so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    # print("Hello",kwargs['first'],kwargs['middle'],kwargs['last'])
    print('Hello',end=' ')
    for key,value in kwargs.items():
        print(value,end=' ')


hello(first='htet',last='aung',middle='moe',title='Mr.')