#type casting = convert the data type of a value to another data type.

x = 1 #int
y = 2.0 # float
z = "3" #str

print(x)
print(y)
print(z)
print(z*3) # returns 333 becoz we cannot perform operations on str data type 

# converting or type casting y and z into int data type
print(int(y)) # temporary change
print(int(z)* 3) # this retuen 3*3 = 9 becoz now it is a int type and can perform operation on it

# want to have a permanent change resign them like
y = int(y)
print(y)

# convert into float
print(float(x))
print(float(z))

#convert into str type
print(str(x))
print(str(y))

#where type casting is used
print("The value of X is " +str(x)) # you cannot noramlly display a string along with an integer or a float becoz we are using some string concatenation
