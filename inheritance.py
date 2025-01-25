class Animal:
    alive = True
    
    def eat(self):
        print("This animal is eating")
        
    def sleep(self):
        print("This animal is Sleeping")
        
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
        
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
rabbit.eat()
rabbit.sleep()
fish.swim()
fish.eat()
fish.sleep()
hawk.fly()
hawk.eat()
hawk.sleep()