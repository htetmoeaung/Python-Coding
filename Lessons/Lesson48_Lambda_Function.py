# Lambda Function = function written in 1 line using lambda keyword
#                   accepts any numbers of argument, but only have one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw away)
#
# lambda paremeter:expression

double = lambda x: x * 2
multiply = lambda x,y: x * y
add = lambda x,y,z: x + y + z
full_name = lambda fname,lname: fname+' '+lname
age_check = lambda age:True if age >= 18 else False

print(double(5))
print(multiply(2,5))
print(add(5,5,3))
print(full_name('luffy','taro'))
print(age_check(17))