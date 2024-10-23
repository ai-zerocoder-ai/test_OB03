import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        animal_type = data.get("type")
        name = data.get("name")
        age = data.get("age")

        if animal_type == "Bird":
            return Bird(name, age)
        elif animal_type == "Mammal":
            return Mammal(name, age)
        elif animal_type == "Reptile":
            return Reptile(name, age)
        else:
            return cls(name, age)

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

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        pass

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "position": self.position
        }

    @classmethod
    def from_dict(cls, data):
        employee_type = data.get("type")
        name = data.get("name")
        position = data.get("position")

        if employee_type == "ZooKeeper":
            return ZooKeeper(name)
        elif employee_type == "Veterinarian":
            return Veterinarian(name)
        else:
            return cls(name, position)

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

    def to_dict(self):
        data = super().to_dict()
        return data

    @classmethod
    def from_dict(cls, data):
        name = data.get("name")
        return cls(name)

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

    def to_dict(self):
        data = super().to_dict()
        return data

    @classmethod
    def from_dict(cls, data):
        name = data.get("name")
        return cls(name)

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

    def to_dict(self):
        return {
            "animals": [animal.to_dict() for animal in self.animals],
            "employees": [employee.to_dict() for employee in self.employees]
        }

    @classmethod
    def from_dict(cls, data):
        zoo = cls()
        animals_data = data.get("animals", [])
        employees_data = data.get("employees", [])

        for animal_data in animals_data:
            animal = Animal.from_dict(animal_data)
            zoo.add_animal(animal)

        for employee_data in employees_data:
            employee = Employee.from_dict(employee_data)
            zoo.add_employee(employee)

        return zoo

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
        print(f"Zoo state saved to {filename}.")

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            zoo = cls.from_dict(data)
            print(f"Zoo state loaded from {filename}.")
            return zoo
        except FileNotFoundError:
            print(f"File {filename} not found. Creating a new zoo.")
            return cls()
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Creating a new zoo.")
            return cls()

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
        animal.eat()

if __name__ == "__main__":
    filename = "zoo_state.json"

    zoo = Zoo.load_from_file(filename)

    if not zoo.animals and not zoo.employees:
        bird = Bird("Vorona", 3)
        mammal = Mammal("Tiger", 5)
        reptile = Reptile("Crocodile", 2)

        zoo.add_animal(bird)
        zoo.add_animal(mammal)
        zoo.add_animal(reptile)

        keeper = ZooKeeper("Ivan")
        vet = Veterinarian("Anna")
        zoo.add_employee(keeper)
        zoo.add_employee(vet)

    print("\nAnimal Sounds:")
    animal_sound(zoo.animals)

    print("\nEmployee Actions:")
    for employee in zoo.employees:
        if isinstance(employee, ZooKeeper):
            for animal in zoo.animals:
                employee.feed_animal(animal)
        elif isinstance(employee, Veterinarian):
            for animal in zoo.animals:
                employee.heal_animal(animal)

    zoo.save_to_file(filename)
