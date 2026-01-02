class Employee:
    language = "python" # This is class attribute
    salary = 1200000
    
    def __init__(self, name, language, salary):
        print("Work is Better") # dundar method which start from underscore
        self.name = "Faizan"
        self.language = 130000
        self.salary = "JavaScript"
    
    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")
    


faizi = Employee("Faizan", 130000, "JavaScript")
# faizi.name = "Faizan"
print(faizi.name, faizi.language, faizi.salary)

# faizi.getInfo()
# faizi.greet()