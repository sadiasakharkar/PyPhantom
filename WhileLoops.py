# while loop = a statement that will execute a block of code as long as it's condition remains true

# QUESTION : create a program to prompt user to enter name , if they don't type in anyhting then we will continue to promt them to type in 
name = None

while not name :
    name = input("Enter your name: ")
    
print("Hello " +name)

