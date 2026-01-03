from random import randint

class Train:
    
    def __init__(slf, TrainNo):
        slf.TrainNo = TrainNo
        
    def book(faizi, fro, to):
        print(f"The Train is book in {faizi.TrainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"The Train is running {self.TrainNo}")
        
    def getFear(self, fro, to):
        print(f"The Train is book in {self.TrainNo} from {fro} to {to} from {randint(222, 5555)}")
        
a = Train("Pindi Express")
a.book("Karachi", "Lahore")
a.getStatus()
a.getFear("Karachi", "Lahore")