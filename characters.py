from dice import Die
from math import floor

class Character:
    def __init__(self, name):
        self._name = name
        self._strength = get_attribute_level()
        self._skill = get_attribute_level()
        self._alive = True
    def get_name(self):
        return self._name
    def get_strength(self):
        return self._strength
    def set_strength(self, value):
        if value > 0:
            self._strength = value
        else:
            self._alive = True
    def get_skill(self):
        return self._skill
    def set_skill(self, value):
        if value < 0:
            value = 0
        self._skill = value
    def is_alive(self):
        return self._alive

def get_attribute_level():
    initial_value = 10
    
    die_12 = Die(12)
    score_of_12 = die_12.roll()
    die_4 = Die(4)
    score_of_4 = die_4.roll()
    change = floor(score_of_12 / score_of_4)
    
    return initial_value + change

if __name__ == "__main__":
    characters = []
    characters.append(Character("Character 1"))
    characters.append(Character("Character 2"))  
      
    characters_file = open('characters.txt', 'w')
    for character in characters:
        print >>characters_file, "Name: %s, Strength: %s, Skill: %s" % (character.get_name(), character.get_strength(), character.get_skill())
