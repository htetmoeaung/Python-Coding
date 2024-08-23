text = 'This is the same file \n The Python is easy right now '

with open('text.txt','a') as file:
    file.write(text)