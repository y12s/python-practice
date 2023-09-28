name = input("please enter your name: ")
age = input("please enter your age : ")
sex = input("please enter your gender: ")
class Train:
    def __init__(self, name1, fare, seats):
        self.name1 = name1 
        self.fare = fare 
        self.seats = seats 
    def getTrainInfo(self):
        print("**************")
        print(f"the name of the train is {self.name1}")
        print(f"the fare of the train is {self.fare}")
        print(f"seats available in the train {self.seats}")
        print("**************")

    def getTicketStatus(self, name):
        if (self.seats>0):
            print("**************")
            print(f"congratulations mr./mrs. {self.name}, your ticket in vande bharat express is succesfully booked. your seat number is {self.seats}")
            print("**************")

            self.seats = self.seats - 1
        else:
            print("**************")
            print("sorry! this train if full! kindly try in tatkal")
            print("**************")

    @staticmethod 
    def greet():
        print(f"Good morning mr./mrs. {name}")
    
    def Ticket(self, name, age, sex):
        self.name = name 
        self.age = age 
        self.sex = sex 

    

person = Train("Vande Bharat Express", "1100 Rs.", 300)
person.greet()
person.getTrainInfo()
person.Ticket(name, age, sex)
person.getTicketStatus(name)
person.getTrainInfo()