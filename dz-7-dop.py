class StudentSimulator:
    def __init__(self, name, total_days):
        self.name = name   
        self.total_days = total_days 
        self.current_day = 0 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.current_day < self.total_days:
            self.current_day += 1  
            return f"День {self.current_day}: {self.name} учится и делает уроки."
        else:
            raise StopIteration

student = StudentSimulator("Али", 3) 

for day in student:
    print(day)
