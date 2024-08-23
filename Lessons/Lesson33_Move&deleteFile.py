import os
import shutil

# source = 'text.txt' # you can also move the folder
# destination = 'C:\\Users\\user\\Desktop\\Web Coding\\move.txt'
#
# try:
#     if os.path.exists(destination):
#         print('The file is already there')
#     else:
#         os.replace(source,destination)
#         print('The file was moved')
# except FileNotFoundError:
#     print(source,'was not there')


# How to delete a file with PYTHON
folder = 'C:\\Users\\user\\Desktop\\New folder'
path = 'text.txt'
try:
    # os.remove(path)
    # os.rmdir(folder) # can only delete the empty folder
    shutil.rmtree(folder) # can delete all files inside the folder and folder itself
except FileNotFoundError:
    print(path,'is not there')
except PermissionError:
    print('You do not have permission to delete it')
except OSError:
    print('Folder is not empty')
else:
    print(folder+' was deleted')