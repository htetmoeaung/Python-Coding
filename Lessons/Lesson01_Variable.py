# variable = a reusable container for storing a value
# a variable behaves as if it were the value it contains

# String DataType
first_name = 'jack'
last_name = 'frost'

fullname = first_name +' '+ last_name
print('Hello '+ fullname)
print('Hello', fullname)

# find the length of your string
print(len(fullname))

# print the datatype of the variable
print(type(fullname))

# Integer DataType (Whole Number)
age = 20
age += 1
# age = age + 1
# print(age)

# need to type cast to display integer with string
print('Your age is: '+str(age))

print('Your age ', age)

# Float DataType (Decimal)
height = 193.4

print('Your height is: '+str(height)+"cm")
print(type(height))

# Boolean DataType (True / False)
human = True
print(type(human))
print('Are you a human: '+str(human))

print(fullname,age,height,human)

# multiple assignment = allow us to assign multipe variable at the same time in one line
luffy = zoro = nami = sanji = ussopp = 18
print(luffy,zoro,nami,sanji)

