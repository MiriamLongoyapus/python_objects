


    # make="Nissan"
    # model="Serena"
    # color="grey"
    # regestrationNo="345N"
class Car:
    def __init__(self,make,model,color,registrationNo):
     self.make=make
     self.model=model
     self.color=color
     self.registrationNo=registrationNo
    def awesome_car(self):
     return f"I love {self.make},{self.model}which is{self.color} in color with{self.registrationNo} because it is a new model and comfortable"
