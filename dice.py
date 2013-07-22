from random import randint
from rpg import get_yes_no

class SidesNotNumberError(ValueError):
    pass

class IllegalSidesError(ValueError):
    pass

class Die:
    def __init__(self, sides):
        if not isinstance(sides, int):
            if not sides.isdigit():
                raise SidesNotNumberError
            sides = int(sides)
            
        if not (sides == 4 or sides == 6 or sides == 12):
            raise IllegalSidesError
        
        self._sides = sides
    
    def get_sides(self):
        return self._sides    
    
    def roll(self):
        return randint(1, self.get_sides())


def create_die_for_user():
    print """You need to set the number of sides for the dice.
How many sides do you want?"""
    
    sides = raw_input()
    
    try:
        return Die(sides)
    except SidesNotNumberError:
        print "Sides must be a positive, whole number!"
        return create_die_for_user()
    except IllegalSidesError:
        print "Sides must be 4, 6 or 12"
        return create_die_for_user()

def play():
    die = create_die_for_user()
    score = die.roll()
    print "%d sided dice thrown, score %d" % (die.get_sides(), score)

    keep_playing = get_yes_no("Do you want to keep playing?")
    
    if keep_playing:
        play()


if __name__ == "__main__":
    play()
