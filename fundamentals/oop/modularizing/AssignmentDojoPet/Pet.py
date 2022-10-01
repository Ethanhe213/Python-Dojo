class Pet():
    def __init__(self,type,tricks,health,energy):
        self.type=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.health+=10
        self.energy+=5
        return self
    def play(self):
        self.health+=5
    def noise(self):
        print("Mewmew")

Cat_D=Pet("Ground","Dodge",100,50)

class Dog(Pet):
    def __init__(self,health,energy,weight):
        super().__init__(health,energy)
        self.weight=weight

Byrant=Dog(100,70,100)
