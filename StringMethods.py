name = "sadia"
#print(len(name))

print(name.find("s")) # find the index of the character specified
print(name.find("d"))
#index start from 0

print(name.capitalize())
print(name.upper())
print(name.isdigit()) # this will return false

num_str = "123"
print(num_str.isdigit()) #this will return true

print(name.isalpha()) # to check if our string contain only letters (if we have space between our string input it will return false)
print(name.count("a"))
print(name.replace("a" , "x"))
print(name*5)