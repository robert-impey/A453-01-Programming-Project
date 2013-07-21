from random import randint
from math import floor

class Character:
    def __init__(self, name):
        self._name = name
        self._strength = get_attribute_level()
        self._skill = get_attribute_level()
    def get_name(self):
        return self._name
    def get_strength(self):
        return self._strength
    def get_skill(self):
        return self._skill

def get_attribute_level():
    initial_value = 10
    
    score_of_12 = randint(1, 12)
    score_of_4 = randint(1, 4)
    change = floor(score_of_12 / score_of_4)
    
    return initial_value + change

if __name__ == "__main__":
    characters = []
    characters.append(Character("Character 1"))
    characters.append(Character("Character 2"))  
      
    characters_file = open('characters.txt', 'w')
    for character in characters:
        print >>characters_file, "Name: %s, Strength: %s, Skill: %s" % (character.get_name(), character.get_strength(), character.get_skill())
