import os

source = "//Users//doctor//Downloads//test//test2.txt"
destination = " //Users//doctor//Downloads//test//copy//copy2.txt"

try:
    if os.path.exists(destination):
        print("There is alreaady a file there")
    else:
        os.replace(source , destination)
        print(source + " was moved")
    
except FileNotFoundError:
    print(source + " was not found")
