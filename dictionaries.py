# dictionary = a changeable , unordered collection of unique key:value pairs Fast because they use hashing, allows us to access a value quickly

capitals = {'USA':'Washington DC' , 
            'India':'New Delhi', 
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'}) # pretended to have LAS VEGAS as a capital

# pop and clear methods
capitals.pop('China')
#capitals.clear()

print(capitals['Russia'])
print(capitals['India'])
print(capitals.get('germany')) #made use of get method to check whether we have the elemnt in our dictonary or not 

print(capitals.keys()) # only the keys not the values
print()
print(capitals.values()) # prints only the values not the keys
print()
print(capitals.items()) # prints the entire dict.

print()

for key,value in capitals.items():
    print(key, value)
    
