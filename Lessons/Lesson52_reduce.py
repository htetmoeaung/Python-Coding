# reduce() = apply a function to a iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeat process until 1 process remain

# reduce(function,iterable)

import functools

letters = ['H','E','L','L','O']
word = functools.reduce(lambda x, y : x + y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda a,b:a*b,factorial)
print(result)

