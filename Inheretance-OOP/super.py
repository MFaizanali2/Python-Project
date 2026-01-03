class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = "intern"


class Programmer(Employee):
    def __init__(self):
         print("Constructor of Programmer")
    b = "Junior"   

  
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = "Senior"
    

# o = Employee()
# print(o.a) 


# o = Programmer()
# print(o.a, o.b) 


o = Manager()
print(o.a, o.b, o.c) 