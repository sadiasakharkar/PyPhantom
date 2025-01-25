# list = used to store multiple items in a single variable 

food = ["pizza" , "hamburger " , "hotdog" , "spaghetti", "cake" , "momos"]
print(food)
print(food[0]) # index of element to be accessed

food[0] = "sushi"
print(food[0])
print()

food.append("ice-cream")
food.remove("hotdog")
food.pop()
food.insert(0 , "pudding")
print()

food.sort()

for x in food:
    print(x)