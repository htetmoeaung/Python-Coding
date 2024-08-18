# List = used to store multiple items in a single variable

food = ['pizza','hamburger','hotdog','ice-cream','pudding','Pepsi']

food[2] = 'fried chickens'

food.append('Coca Cola')
food.remove('pudding')
food.pop() # remove the last item of the list
food.sort()
# food.clear() # remove all the items of the list

for i in food:
    print(i,'',end='')
