class Employee:
    company = "AMC"
    
    def detail(self):
        print(f"The name of Employee is {self.company} and the language is {self.language}")

class coder:
    language = "Python"
    def showLanguage(self):
        print(f"Your Language is {self.language}")
       
class Program(Employee, coder):
    company = "AMC"
    
    def detail2(self):
        print(f"The name of Employee is {self.company} and the language is {self.language}")
    
    
a = Employee()
b = Program()

b.detail()
b.showLanguage()
b.detail2()

# print(a.company, b.company)