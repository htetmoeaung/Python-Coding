# Nested Loop = the inner loop will finish all of it's iterations
#               before finishing one iterations of the outer loop

# rows = int(input('How many rows?: '))
# columns = int(input('How many columns?: '))
# symbol = input('Enter a symbol to use: ')
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end='')
#     print()

rows = 5

# Pyramid
# for i in range(rows):
#     for c in range(rows - i - 1):
#         print(' ',end='')
#     for k in range(2*i+1):
#         print('*',end='')
#     print()

# for i in range(rows):
#     for c in range(rows-i):
#         print(' ',end='')
#     for k in range(i+1):
#         print('*',end='')
#     print()

for i in range(rows):
    for c in range(i):
        print(' ',end='')
    for k in range(rows-i):
        print('*',end='')
    print()







# for i in range(1,5+1,1):
#     for c in range(i):
#         print('*',end='')
#     print()
#
# for j in range(5,0,-1):
#     for k in range(j):
#         print('*',end='')
#     print()

