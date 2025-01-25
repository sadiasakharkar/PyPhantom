#index operator [] = gives access to a sequence's element (str , list , tuples)

name = "sadia sakharkar!"

if(name[0].islower()):
    name = name.capitalize()
    
print(name) 

first_name = name[0:5].upper()
print(first_name)

last_name = name[6:].upper()
print(last_name)

last_character = name[-1] #last element 
print(last_character)

second_last = name[-3]
print(second_last)

