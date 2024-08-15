# tuple = collection which is ordered and unchangeable
#         used to group related date

student = (1,'Htet Moe Aung',20,'male',20)

print(student.count(20))
print(student.index('male'))

for x in student:
    print(x,end=', ')


if 'Htet Moe Aung' in student:
    print('He is Here')