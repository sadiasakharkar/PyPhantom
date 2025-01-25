# walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assign values to variable as part of a larger expression

# happy = True
# print(happy)

print(happy := True)

# food = []
# while True:
#     item = input("What do you like? ")
#     if item == "quit":
#         break
#     food.append(item)
 
# above code using the walrus operator 


food = []
while item := input("What food do you like? ") != "quit":
    food.append(item)
 