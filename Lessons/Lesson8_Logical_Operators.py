# Logical Operators (and,or,not) = used to check if two or more
#                                  conditional statement is true

temp = int(input('What is the temperature outside?: '))

# and = only work if both condition are true
# or = work if one of the condition is true

if temp >= 0 and temp <= 30:
    print('the temperature is good today')
elif temp > 0 or temp < 30:
    print('the temperature is bad today')


# not = change the opposite of true or false
a = 2
b = 2
print(not(a == b))