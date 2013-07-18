from random import randint
import math

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

characters = []
characters.append(make_character("Character 1"))
characters.append(make_character("Character 2"))

characters_file = open('characters.txt', 'w')

for character in characters:
    print>>characters_file, character
