class Human:
    def __init__(self, name):
        self.name = name 
    
    def say_hello(self):
        print("Привет, меня зовут", self.name)

class Pet:
    def __init__(self, name):
        self.name = name 
    
    def play(self):
        print(self.name, "играет с хозяином")

          
human = Human("Али") 
pet = Pet("Барсик")

human.say_hello()
pet.play()
