import re
from random import randint

print """Welcome to the game!
You need to set the number of sides for the dice."""

sides = False
sides_regex = re.compile("^(4|6|12)$")

while not sides:
    print """
You can have 4, 6 or 12 sides
How many sides do you want?"""

    sides_raw = raw_input()
    
    if sides_regex.match(sides_raw):
        sides = int(sides_raw)

keep_playing = True
keep_playing_regex = re.compile("^y(es)?$", re.IGNORECASE)

while keep_playing:
    score = randint(1, sides)
    print "%d sided dice thrown, score %d" % (sides, score)
    
    print "Do you want to keep playing?"
    keep_playing_raw = raw_input()
    
    keep_playing = keep_playing_regex.match(keep_playing_raw)
