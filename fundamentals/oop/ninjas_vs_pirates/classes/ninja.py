class Ninja:

    def __init__(self,name,strength,speed,health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health 
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    def self_heal(self):
        self.health+=30
class BlackDress(Ninja):
    def __init__(self, name, strength, speed, health):
        super().__init__(name, strength, speed, health)
   
