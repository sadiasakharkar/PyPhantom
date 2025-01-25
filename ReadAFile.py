try:
    with open('//Users//doctor//Downloads//test//test.txt') as file :
      print(file.read())
    
   # print(file.closed)
        
except:
    print("The file was not found")