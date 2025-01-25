# str.format() = optional method that gives users more control when displaying output

animal = "Cow"
item = "moon"

#print("The " + animal + " jumped over the "+ item)
print("The {} jumped over the {}".format("Cow" , "Moon"))
# or
print("The {} jumped over the {}".format(animal , item))
print("The {0} jumped over the {1}".format(animal , item)) # positional arguments (we can reuse the same index)
print("The {1} jumped over the {0}".format(animal , item))
#print("The {} jumped over the {}".format(animal="Cow" , item =" Moon")) #keyword argument (we can use keyword more than once)

text = "The {} jumped over the {}"
print(text.format(animal , item))

name = "Sadia"
print("Hello, my name is {:10} nice to meet you".format(name))
print("Hello, my name is {:>10} nice to meet you!".format(name)) # right align 
print("Hello, my name is {:<10} nice to meet you!".format(name)) # left align
print("Hello, my name is {:^10} nice to meet you!".format(name)) # center align

#print("Hello, my name is {name:>7} nice to meet you!".format(name)) # need to add positional or keyword argument just preceed the colon 

number = 3.14159

print("The number pi is {:.2f}".format(number)) # prints only 2 digits after the decimal

number = 1000
print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) #bianary notation
print("The number is {:o}".format(number)) # octal notation
print("The number is {:x}".format(number)) #hexadecimal (lower case)
print("The number is {:X}".format(number)) #hexadecimal (upper case)
print("The number is {:e}".format(number)) #scientific notation (lower case)
print("The number is {:E}".format(number)) # scientfic notation (upper case)