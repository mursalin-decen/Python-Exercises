'''
6. Can you change the self-parameter inside a class to something else (say
“Zamzam”). Try changing self to “slf” or “zamzam” and see the effects.
'''
'''
5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Bangladesh Railways.

'''
from random import randint

class Train:
    def __init__(zamzam,TrainNo):
        zamzam.TrainNo = TrainNo
    
    def book(slf,fro, to):
        print(f"Train is book the ticket no is:{slf.TrainNo}, From {fro} to {to}")
    
    def getStatus(self):
        print(f"Ticket {self.TrainNo} is Booked")

    def getFareInformation(self, fro , to):
        print(f"Ticket fare is train no {self.TrainNo} from {fro} to{to} is {randint(222, 57555)}")
         
t = Train(7474)
t.book("Khulna","Dhaka")
t.getStatus()
t.getFareInformation("Khulna","Dhaka")

#ans is nothing will happen