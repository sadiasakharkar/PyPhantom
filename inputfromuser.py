#https://youtu.be/8lPEwiKqKfY?si=NSnKtyHm2MUoPP4h

name = input("Enter your name : ") #by default input type is str 
print("Hello "+name)

age = input("Enter your age : ")
print("Your age is "+ str(age))

nextage = int(input("Enter your current age: ")) # we have immediately converted into int data type as it is in str by default 
nextage = nextage + 1 # operations can be performed on int datatype 
print("You will be " + str(nextage) + " years old next birthday") #while printing we have converted back into str data type , as we cannot concate int with str 