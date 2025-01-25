# Prevent a user from creating an object of that class
# + compiles a user to override abstract method in a child class. 

# abstract class = a class which contains one or more abstract method.
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC , abstractmethod  # abc - abstract based class

class Vehical(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    
    def go(self):
        print("You drive the car")
        
    def stop(self):
            print("This car is stopped")
    
class Motorcycle(Vehical):
    
    def go(self):
        print("You ride the motorcycle")
        
    def stop(self):
            print("This motorcycle is stopped")
        
# vehical = Vehical()
car = Car()
motorcycle = Motorcycle()

# vehical.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

