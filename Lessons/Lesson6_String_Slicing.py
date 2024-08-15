# Slicing = creating substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = 'Htet Moe Aung'

first_name = name[0:4]
middle_name = name[5:8]
last_name = name[9:]
reversed_name = name[::-1]

print(first_name,middle_name,last_name,reversed_name)

website = 'https://google.com'
website2 = 'https://wikipedia.com'

slice = slice(8,-4)

print(website[slice])
print(website2[slice])