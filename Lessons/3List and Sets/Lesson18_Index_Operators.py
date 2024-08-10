# Index Operators [] = give access to a sequence's element
#                      (str,list,tuples)

name = 'htet moe?'

if(name[0].lower()):
    name = name.capitalize()
print(name)

first_name = name[0:4].upper()
last_name = name[5:].upper()
last_char = name[-1]

print(first_name)
print(last_name)
print(last_char)

print()



