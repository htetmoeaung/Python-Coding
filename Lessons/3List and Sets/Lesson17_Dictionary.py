# Dictionary = a changeable, unordered collection of unique key:value pairs
#              Fast because they used hashing, allow us to access a value quickly

capitals = {'Myanmar':'Yangon',
            'USA':'Washington DC',
            'Japan':'Tokyo',
            'Russia':'Mosocow'
            }

capitals.update({'South Korea':'Seoul'})
capitals.update({'USA':'New York'})
capitals.pop('Russia')
#capitals.clear()

print(capitals['Japan'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)

