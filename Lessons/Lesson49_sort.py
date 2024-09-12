# sort() method   = used with lists
# sort() function = used with iterables

# fruits = ('mango','watermelon','coconut','apple','lemon')
# fruits1 = ['mango','watermelon','coconut','apple','lemon']
#
# fruits1.sort(reverse=True)
# sorted_fruits = sorted(fruits,reverse=True)
#
# for i in sorted_fruits:
#     print(i)

students = [
    ('Squidward','F',60),
    ('Sandy','D',33),
    ('Patrick','D',36),
    ('Spongebob','B',20),
    ('Mr.Krabs','C',78)
]
grade = lambda grades:grades[1]
age = lambda age:age[2]
students.sort(key=grade)

sorted_stds = sorted(students,key=age,reverse=True)

for i in students:
    print(i)
print('--------------')
for j in sorted_stds:
    print(j)
