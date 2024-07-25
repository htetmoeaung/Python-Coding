# Nested Loop = the inner loop will finish all of it's iterations
#               before finishing one iterations of the outer loop

rows = int(input('How many rows?: '))
columns = int(input('How many columns?: '))
symbol = input('Enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()