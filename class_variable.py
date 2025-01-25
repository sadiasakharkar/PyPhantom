class Car:
    
    wheels = 4 #class variable
    
    # special method that creates object for us called the 'init method' in another programming language this is known as construtor
    def __init__(self , make , model , year , color): #synatx is : def __init__() 'two underscore'
        self.make = make # self here works as "this. " in java
        self.model = model #instance variables
        self.year = year
        self.color = color
        
car_1 = Car("Chevy" , "Corvette" , 2021 , "Blue")
car_2 = Car("Ford" , "Mustang" , 2022 , "Red")

# car_1.wheels = 2
Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)

# print(Car.wheels)