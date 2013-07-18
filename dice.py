from random import randint

def get_sides():
    print """
You can have 4, 6 or 12 sides
How many sides do you want?"""
    
    sides_raw = raw_input()
    
    sides = int(sides_raw)

    if sides == 4 or sides == 6 or sides == 12:
        return sides
    else:
        return get_sides()

def get_yes_no(question):
    print question
    
    answer = raw_input()
    
    if answer.upper() == 'Y' or answer.upper() == "YES":
        return True
    elif answer.upper() == 'N' or answer.upper() == "NO":
        return False
    else:
        print "Please enter either 'Y(es)' or 'N(o)'"
        return get_yes_no(question)

def play():
    sides = get_sides()
    
    score = randint(1, sides)
    print "%d sided dice thrown, score %d" % (sides, score)

    keep_playing = get_yes_no("Do you want to keep playing?")
    
    if keep_playing:
        play()

print """Welcome to the game!
You need to set the number of sides for the dice."""
play()
