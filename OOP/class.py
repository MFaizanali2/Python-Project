class Employee:
    language = "python" # This is class attribute
    salary = 1200000
    
data = Employee()
data.name = "Faizan"
print(data.name, data.language, data.salary)

faizi = Employee()
faizi.name = "shayan" # This is instance attribute
print(faizi.salary, faizi.language, faizi.name)