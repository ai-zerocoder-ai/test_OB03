class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Karrr")

    def eat(self):
        print(f"{self.name} eats bread.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says: Grrrr")

    def eat(self):
        print(f"{self.name} eats meat.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says: Sssss")

    def eat(self):
        print(f"{self.name} eats birds.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
        animal.eat()

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} as {employee.position}.")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        pass

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


zoo = Zoo()

bird = Bird("Vorona", 3)
mammal = Mammal("Tiger", 5)
reptile = Reptile("Crocodile", 2)

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

animal_sound(zoo.animals)

keeper = ZooKeeper("Ivan")
vet = Veterinarian("Anna")

zoo.add_employee(keeper)
zoo.add_employee(vet)

keeper.feed_animal(mammal)
vet.heal_animal(reptile)
