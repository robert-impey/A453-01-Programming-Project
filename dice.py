import re
from random import randint

def get_sides():
    while True:
        print """
You can have 4, 6 or 12 sides
How many sides do you want?"""
        
        sides_raw = raw_input()
        
        sides = int(sides_raw)
    
        if sides == 4 or sides == 6 or sides == 12:
            return sides

print """Welcome to the game!
You need to set the number of sides for the dice."""

sides = get_sides()

keep_playing = True
keep_playing_regex = re.compile("^y(es)?$", re.IGNORECASE)

while keep_playing:
    score = randint(1, sides)
    print "%d sided dice thrown, score %d" % (sides, score)
    
    print "Do you want to keep playing?"
    keep_playing_raw = raw_input()
    
    keep_playing = keep_playing_regex.match(keep_playing_raw)
