# 19
import os

path = 'C:\\Users\\user\\Desktop\\Resources\\test.txt'

if os.path.exists(path):
    print('That location exist')
    if os.path.isfile(path):
        print('This is a File')
    elif os.path.isdir(path):
        print('This is a Folder or Directory')
else:
    print("That location doesn't exist")
