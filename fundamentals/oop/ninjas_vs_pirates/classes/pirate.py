import random
class Pirate:

    def __init__( self , name,strength,speed,health ):
        self.name = name
        self.strength = strength
        self.speed = speed 
        self.health = health
        

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self
    def special_attack(self,ninja):
        ninja.health=ninja.health-self.special_move
    
class caribbean(Pirate):
    def __init__(self, name, strength, speed, health,special_move):
        super().__init__(name, strength, speed, health)
        self.special_move=special_move
class atlantic(Pirate):
    def __init__(self, name, strength, speed, health):
        super().__init__(name, strength, speed, health)
       
    def pierce_attack(self,ninja):
        if random.randrange(1,4)==3 or random.randrange(1,4)==2:
            ninja.health=ninja.health-self.strength*2
        else:pass
