class Car:
    
    # special method that creates object for us called the 'init method' in another programming language this is known as construtor
    def __init__(self , make , model , year , color): #synatx is : def __init__() 'two underscore'
        self.make = make # self here works as "this. " in java
        self.model = model
        self.year = year
        self.color = color
        
    def drive(self):
        print("This "+self.model+" is driving")
        
    def stop(self):
        print("This "+self.model+" is stopped")
        
car_1 = Car("Chevy" , "Corvette" , 2021 , "Blue")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

print()

car_2 = Car("Ford" , "Mustang" , 2022 , "Red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()