# Write a class train which has methods to book a ticket, get status(no. of seats) and get fare information of trian running under the railways

from random import randint
class Train:
    def __init__(self , TrainNo):
        self.TrainNo = TrainNo
        
    def book(self , fro , to):
        print(f"Ticket is booked in train no: {self.TrainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No: {self.TrainNo} is running on time.")

    def getFare(self, fro , to):
        print(f"Ticket fare in train no: {self.TrainNo} from {fro} to {to} is {randint(222, 5555)}")

t= Train(12322)
t.book("Karachi" , "Islamabad")
t.getStatus()
t.getFare("Karachi" , "Islamabad")