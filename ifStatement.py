# if statement = a block of code that will execute if it's conditon is true
age = int(input("Enter your current age : "))


if age == 100:
    print("YOU ARE A CENTURY OLD!!🎉")
elif age >= 18:
        print("You are an adult!")
elif age <0:
    print("You haven't been born yet!")
else:
    print("You are a minor!")