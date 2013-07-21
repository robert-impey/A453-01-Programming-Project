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

def calculate_attribute_modifier(character_attribute_1, character_attribute_2):
    difference = abs(character_attribute_1 - character_attribute_2)
    
    modifier = floor(difference / 5)
    
    return modifier
 
def encounter(character_1, character_2):
    strength_modifier = calculate_attribute_modifier(character_1.get_strength(), character_2.get_strength())
    skill_modifier = calculate_attribute_modifier(character_1.get_skill(), character_2.get_skill())
    
    die = Die(6)
    die_score_1 = die.roll()
    die_score_2 = die.roll()
     
    if die_score_1 != die_score_2:
        if die_score_1 > die_score_2:
            character_1.set_strength(character_1.get_strength() + strength_modifier)
            character_1.set_skill(character_1.get_skill() + skill_modifier)
            character_2.set_strength(character_2.get_strength() - strength_modifier)
            character_2.set_skill(character_2.get_skill() - skill_modifier)
        else:
            character_1.set_strength(character_1.get_strength() - strength_modifier)
            character_1.set_skill(character_1.get_skill() - skill_modifier)
            character_2.set_strength(character_2.get_strength() + strength_modifier)
            character_2.set_skill(character_2.get_skill() + skill_modifier)

if __name__ == "__main__":
    characters = []
    characters.append(Character("Character 1"))
    characters.append(Character("Character 2"))  
      
    characters_file = open('characters.txt', 'w')
    for character in characters:
        print >>characters_file, "Name: %s, Strength: %s, Skill: %s" % (character.get_name(), character.get_strength(), character.get_skill())
