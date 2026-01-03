class programmer:
    company = "AMC"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
        
user = programmer("Faizan", 60000, 7500)
print(user.company, user.name, user.salary, user.pin)

user2 = programmer("Umair", 80000, 7500)
print(user2.company, user2.name, user2.salary, user2.pin)