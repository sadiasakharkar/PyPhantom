# set = collection which is unordered , unindexed. No duplicate values

utensils = {"fork" , "spoon" , "knife" , "knife"}

utensils.add("Napkin")
utensils.remove("knife")
#utensils.clear()
print()

for x in utensils:
    print(x)

dishes = { "bowl" , "plate" , "cup" , "knife"}

utensils.update(dishes)

for i in utensils:
    print(i)

print()

dishes.update(utensils)
for z in dishes:
    print(z)

print()
    
dinner_table = utensils.union(dishes)
for a in dinner_table:
    print(a)

print()
    
print(dishes.difference(utensils))
print(utensils.intersection(dishes))