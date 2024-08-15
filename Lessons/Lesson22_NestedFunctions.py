# Nested Functions calls = function call inside other function call
#                          innermost function calls are resolved first
#                          return value is used as argument for the next outer function


num = input('Enter a whole positive number: ')
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input('Enter a whole positive number: ')))))