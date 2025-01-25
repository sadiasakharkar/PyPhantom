# below commented are the shutil functions
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadeta (file's creation and modification times)

import shutil

shutil.copyfile('//Users//doctor//Downloads//test//test.txt' , '//Users//doctor//Downloads//test//copy//copy.txt') #src,dst
shutil.copy2('//Users//doctor//Downloads//test//test.txt' , '//Users//doctor//Downloads//test//copy//copy.txt')