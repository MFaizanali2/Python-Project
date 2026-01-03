class calculator:
    
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The Sqaure of n is {self.n * self.n}")
    
    def cube(self):
        print(f"The Sqaure of n is {self.n * self.n * self.n}")          
    
    def squareRoot(self):
        print(f"The Sqaure of n is {self.n ** 1/2}")
        
    @staticmethod
    def greet():
        print("Assalam o Alikum")

a = calculator(6)
a.greet()
a.square()       
a.cube()       
a.squareRoot()