class Employee:
    a = "intern"


class Programmer(Employee):
    b = "Junior"   

  
class Manager(Programmer):
    c = "Senior"
    

o = Employee()
print(o.a) 


o = Programmer()
print(o.a, o.b) 


o = Manager()
print(o.a, o.b, o.c) 