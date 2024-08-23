# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copy metatdata (file's creation and modification time)

import shutil

shutil.copyfile('text.txt','C:\\Users\\user\\Desktop\\Python Coding\\Lessons\\copy.txt')