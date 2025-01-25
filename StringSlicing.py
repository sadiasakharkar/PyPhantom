# Slicing = create a substring by extracting from another string indexing [] or slice() 
# [start:stop:step]
name = "sadia sakharkar"
first_name = name[0:3]
print(first_name)
# first index is inclusive and the stopping index is exclusive 
first_name = name[:5] # another way of writting
print(first_name)

last_name = name[6:15] # can also be written as 
# last_name = name[6:]
print(last_name)

# STEP = step is an optional field that we can set a value to 
# step is how much we are increasing our index by between starting and stoping , it is entirely possible to create a substring that will count only every second(or defined) character after the first , it is one by default 

funky_name = name[0:15:2] # another way of writting is 
# funcky_name = name[::2]
print(funky_name)

#reverse a name 
reversed_name = name[::-1]
print(reversed_name)

# Using a slice function to create a slice object , which are reuseable
website1 = "http://google.com"
# QUESTION: Extract word google from above 

#slice(start , stop , step )
slice = slice(7,-4) #used negative indexing -4 -3 -2 -1 i.e . c o m (negative indexing start from end)
print(website1[slice])

website2  = "http://wikipedia.com"
print(website2[slice])