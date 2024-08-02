# Loop Control Statement = change a loop execution from its normal sequence
# break = used to terminate the loop entirely
# continue = skip to the next iteration of the loop
# pass = do nothing, acts as a placeholder


# while True:
#     name = input('Enter your name: ')
#     if name != '':
#         break

phone_number = '123-456-789'
for i in phone_number:
    if i == '-':
        print('-', end='')
        continue
    print(i,end='')

print()

for j in range(1,21):
    if j == 13:
        pass
    else:
        print(j,' ',end='')