class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Начальный уровень голода
        self.energy = 5  # Начальный уровень энергии

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(self.name + " поел и стал менее голодным!")
        else:
            print(self.name + " не голоден.")

    def sleep(self):
        if self.energy < 10:
            self.energy += 1
            print(self.name + " поспал и набрался сил!")
        else:
            print(self.name + " не хочет спать, у него достаточно энергии!")

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            self.hunger += 1
            print(self.name + " поиграл и немного устал.")
        else:
            print(self.name + " слишком устал, чтобы играть.")

    def status(self):
        print("Голод:", self.hunger)
        print("Энергия:", self.energy)


my_cat = Cat("Уголек")

my_cat.status()
my_cat.eat()
my_cat.play()
my_cat.sleep()
my_cat.status()
