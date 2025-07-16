class Car:
    def __init__(self,model,color,price):
        self.model=model
        self.color=color
        self.price=price
        print(f"the car is {self.model} of {self.color}")
    
    def start(self):
        print(f"You can start {self.model} car")
        
    def turnoff(self):
        print(f"You can turn off {self.model} car")
        
        
car1=Car("Thar","red",500000)
car1.start()
car1.turnoff()

car2=Car("Bolero","black",250000)

#inheritance
class Animal:
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print(f"{self.name} can eat.")
        
    def sleep(self):
        print(f"{self.name} can sleep.")
        
    def drink(self):
        print(f"{self.name} can drink.")
        
class Dogs(Animal):
    def bark(self):
        print("can woof. ")

class Cats(Animal):
    pass

animal1=Dogs("Tyson")  #creating object
animal2=Cats("Belly")

animal1.eat()
animal1.drink()
animal1.bark()

animal2.eat()
animal2.sleep()

