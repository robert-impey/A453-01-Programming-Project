from dice import Die
from math import floor

class Character:
    def __init__(self, name, strength, skill):
        self._name = name
        
        if not (isinstance(strength, int) 
                and isinstance(strength, int)):
            raise ValueError
        self._strength = strength
        self._skill = skill
        
        self._alive = True
        
    def get_name(self):
        return self._name
    
    def get_strength(self):
        return self._strength
    
    def set_strength(self, value):
        if not isinstance(value, int):
            raise ValueError
        if value > 0:
            self._strength = value
        else:
            self._alive = True
            
    def get_skill(self):
        return self._skill
    
    def set_skill(self, value):
        if not isinstance(value, int):
            raise ValueError
        if value < 0:
            value = 0
        self._skill = value
        
    def is_alive(self):
        return self._alive
    
    def to_string(self):
        return ("Name: %s, Strength: %s, Skill: %s, Is alive?: %s" % 
                (self.get_name(), self.get_strength(), 
                 self.get_skill(), self.is_alive()))


def get_attribute_level():
    initial_value = 10
    
    die_12 = Die(12)
    score_of_12 = die_12.roll()
    die_4 = Die(4)
    score_of_4 = die_4.roll()
    change = floor(score_of_12 / score_of_4)
    
    return int(initial_value + change)

def create_character_random_attribute_levels(name):
    return Character(name, get_attribute_level(), get_attribute_level())


if __name__ == "__main__":
    characters = []
    characters.append(create_character_random_attribute_levels("Character 1"))
    characters.append(create_character_random_attribute_levels("Character 2"))  
      
    characters_file = open('characters.txt', 'w')
    for character in characters:
        print >> characters_file, character.to_string()
