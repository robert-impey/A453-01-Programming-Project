from random import randint
import math

def get_sides():
    print """You need to set the number of sides for the dice.
You can have 4, 6 or 12 sides
How many sides do you want?"""
    
    sides_raw = raw_input()
    
    if not sides_raw.isdigit():
        return get_sides()
    
    sides = int(sides_raw)
    
    if not (sides == 4 or sides == 6 or sides == 12):
        return get_sides()
    
    return sides 

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

def get_attribute_level():
    initial_value = 10
    
    score_of_12 = randint(1, 12)
    score_of_4 = randint(1, 4)
    change = math.floor(score_of_12 / score_of_4)
    
    return initial_value + change
    
def make_character(name):
    character = {'name': name}
    
    character['strength'] = get_attribute_level()
    character['skill'] = get_attribute_level()
    
    return character

