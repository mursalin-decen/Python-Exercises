'''
5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Bangladesh Railways.

'''
from random import randint

class Train:
    def __init__(self,TrainNo):
        self.TrainNo = TrainNo
    
    def book(self,fro, to):
        print(f"Train is book the ticket no is:{self.TrainNo}, From {fro} to {to}")
    
    def getStatus(self):
        print(f"Ticket {self.TrainNo} is Booked")

    def getFareInformation(self, fro , to):
        print(f"Ticket fare is train no {self.TrainNo} from {fro} to{to} is {randint(222, 57555)}")
         
t = Train(7474)
t.book("Khulna","Dhaka")
t.getStatus()
t.getFareInformation("Khulna","Dhaka")