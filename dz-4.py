class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} говорит: 'Привет!'"

class Robot:
    def __init__(self, model, battery_level):
        self.model = model
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100
        return f"Робот {self.model} полностью заряжен!"

class CyborgWorker(Human, Robot):
    def __init__(self, name, age, model, battery_level, profession):
        Human.__init__(self, name, age)
        Robot.__init__(self, model, battery_level)
        self.profession = profession

    def work(self):
        if self.battery_level > 10:
            self.battery_level -= 10
            return f"{self.name}, модель {self.model}, работает как {self.profession}."
        else:
            return f"{self.name} требует зарядки! Заряд батареи: {self.battery_level}%."

worker = CyborgWorker("Андрей", 26, "Wd-31", 50, "инженер")
print(worker.speak())
print(worker.charge())
print(worker.work())
print(worker.work())
