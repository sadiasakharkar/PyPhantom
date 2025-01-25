# function = a block of code which is executed only when it is called.

def hello(name):
    print("Hello! "+name )
    print("Have a nice day!")
    
hello("Sadia")
hello("Zikra")

my_name = "Abdullah"
hello(my_name)

def hello(first_name , last_name ):
    print("HEllO!! "+ first_name +" "+last_name) 
    
hello("sadia", "sakaharkar")

print()

def info(name , age , city):
    print("Hello! "+ name)
    print("From the entered data:")
    print("Your age is "+age)
    print("You belongs to "+ city +" city.")

name =input("Enter your name: ")
age = input("Plese enter your age: ")
city = input("Plese enter your city: ")
print()

info(name , age , city)
