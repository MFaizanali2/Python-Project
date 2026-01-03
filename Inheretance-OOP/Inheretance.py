class Employee:
    company = "AMC"
    
    def detail(self, name, age):
        print(f"The name of Employee is {name} and the age is {age}")
        
class Program(Employee):
    company = "AMC"
    
    def detail2(self, name, age):
        print(f"The name of Employee is {name} and the age is {age}")
    
    
a = Employee()
b = Program()

print(a.company, b.company)