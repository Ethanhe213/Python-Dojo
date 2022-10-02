
from classes.ninja import *
from classes.pirate import *

michelangelo = BlackDress("Michelanglo",30,5,85)


jack_sparrow = caribbean("Jack Sparrow",15,5,100,30)
Noname=atlantic("noname",10,5,150)


@staticmethod
def Battle():
    while michelangelo.health>0 and jack_sparrow.health>0 and Noname.health>0:
        if michelangelo.health<30:
            michelangelo.self_heal()
        else:
            michelangelo.attack(jack_sparrow)
            jack_sparrow.special_attack(michelangelo)
            michelangelo.attack(Noname)
            Noname.pierce_attack(michelangelo)
           

    jack_sparrow.show_stats()
    michelangelo.show_stats()
    Noname.show_stats()


Battle()