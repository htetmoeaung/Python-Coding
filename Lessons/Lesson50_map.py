# map = applies a function to each item in an iterable (list, tuple ,etc)

# map(function,iterable)

store = [('shirt',20.00),
         ('shirt',25.00),
         ('shirt',50.00),
         ('shirt',10.00),
         ('shirt',5.00)]

to_eruos = lambda data: (data[0],data[1]*0.82)
to_dollar = lambda data: (data[0],data[1]/0.82)

store_dollars = list(map(to_dollar,store))
store_euros = list(map(to_eruos,store))

for i in store_dollars:
    print(i)
print('---------------')
for j in store_euros:
    print(j)

