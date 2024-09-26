###############################
### Single level Inheritance###
###############################

# Base class
class Polygon:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is a closed shape with n number of sides.")


# Derived class
class Square(Polygon):
    def __init__(self, name, number_of_sides):
        super().__init__(name)
        self.number_of_sides = number_of_sides

    def display(self):
        print(f"{self.name}, the {self.name} polygon has {self.number_of_sides} sides.")


# Example usage
square = Square("Square", "4")
square.display()


###########################
### Multiple Inheritance###
###########################

# Base class 1
class Mammal:
    def mammal(self):
        print("mammal")


# Base class 2
class Flyer:
    def fly(self):
        print("can fly")


# Derived class
class Bat(Mammal, Flyer):
    def __init__(self, name):
        self.name = name

    def abilities(self):
        print(f"{self.name} is both a Mammal and can Fly.")


# Example usage
bat = Bat("Bat")
bat.abilities()
bat.mammal()
bat.fly()




##############################
### Multi Level Inheritance###
##############################


# Base class
class Vehicle:
    def __init__(self, make):
        self.make = make

    def show_make(self):
        print(f"Vehicle make: {self.make}")


# Intermediate derived class
class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model

    def show_model(self):
        print(f"Car model: {self.model}")


# Final derived class
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def show_battery(self):
        print(f"Battery capacity: {self.battery_capacity} kWh")


# Example usage
tesla = ElectricCar("Tesla", "Model S", 100)
tesla.show_make()
tesla.show_model()
tesla.show_battery()
