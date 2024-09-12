# Higher Order Function = a function that either :
#                        1. accept a function as an argument or
#                        2. return a function
#                        (In Python, functions are also treated as an object)

# def loud(text):
#     return text.upper()
# def quiet(text):
#     return text.lower()
# def hello(func):
#     text = func('Hello')
#     print(text)
# hello(loud)
# hello(quiet)

def divisor(x):
    def dividned(y):
        return y / x
    return dividned

divide = divisor(2)
print(divide(10))