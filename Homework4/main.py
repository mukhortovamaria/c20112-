class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    def make_sound(self):
        return "звук"

    def __str__(self):
        return f"{self.species} звуть {self.name}, {self.age} років"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, species="Собака")
        self.breed = breed
    def make_sound(self):
        return "Гав"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, species="Кіт")
        self.color = color
    def make_sound(self):
        return "Мяу"

if __name__ == "__main__":
    dog = Dog(name="Пудж", age=3, breed="Мопс")
    cat = Cat(name="Пушок", age=2, color="Білий")
    print(dog)
    print(dog.make_sound())
    print(cat)
    print(cat.make_sound())
