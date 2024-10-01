# Filter = creates a collection of elements from an iterable
#          for which a function return true

# filter(function,iterable)

crews = [('Luffy',19,'male'),
           ('Nami',20,'female'),
           ('Chopper',17,'deer'),
           ('Zoro',21,'male'),
           ('Sanji',21,'male'),
           ('Robin',30,'female'),
           ('Usopp',19,'male')]

gender = lambda data:data[2] == 'male'

male_crew = list(filter(gender,crews))
for i in male_crew:
    print(i)

