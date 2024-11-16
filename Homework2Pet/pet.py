class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = 50
        self.energy = 50

    def feed(self):
        print(f"{self.name} поїв")

    def play(self):
        if self.energy >= 20:
            self.energy -= 20
            self.hunger += 10
            print(f"{self.name} грається")
        else:
            print(f"{self.name} втомлений для гри")

    def status(self):
        print(f"{self.animal_type} {self.name}— Голод: {self.hunger}, Енергія: {self.energy}")
pet = Pet(name="Пушок", animal_type="Кіт")
pet.status()
pet.feed()
pet.play()
pet.status()