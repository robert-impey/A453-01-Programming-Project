from math import floor
from dice import Die

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
