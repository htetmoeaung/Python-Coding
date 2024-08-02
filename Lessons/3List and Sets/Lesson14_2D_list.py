# 2D List = a list of lists

drinks = ['soda','coffee','tea']
breakfast = ['Fried Egg','Beacon','Toasted Bread']
desert = ['Cake','Ice Cream','Pancake']

food = [drinks,breakfast,desert]

print(food[1][2])

for i in food:
    for j in i:
        print(j,end=' ')
    print()