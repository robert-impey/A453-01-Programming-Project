from characters import Character
from dice import Die
from math import floor
from rpg import get_positive_whole_number_from_user

def make_character_user_set_attribute_levels(name):
    return Character(
                     name,
                     get_positive_whole_number_from_user("Please enter the strength for %s." % name),
                     get_positive_whole_number_from_user("Please set the skill level for %s." % name))

def print_characters(characters):
    for character in characters:
        print character.to_string()

def calculate_attribute_modifier(character_1_attribute, character_2_attribute):
    difference = abs(character_1_attribute - character_2_attribute)
    
    modifier = floor(difference / 5)
    
    return int(modifier)

def encounter(character_1, character_2):
    strength_modifier = calculate_attribute_modifier(
                                                     character_1.get_strength(),
                                                     character_2.get_strength())
    skill_modifier = calculate_attribute_modifier(character_1.get_skill(), character_2.get_skill())
    
    print "Stength modifier: %d" % strength_modifier
    print "Skill modifier: %d" % skill_modifier
    
    die = Die(6)
    die_score_1 = die.roll()
    die_score_2 = die.roll()
    
    print "Die score 1: %d, die score 2: %d" % (die_score_1, die_score_2)
    
    if die_score_1 == die_score_2:
        print "Tie!"
    else:
        if die_score_1 > die_score_2:
            print "Player 1 wins!"
            character_1.set_strength(character_1.get_strength() + strength_modifier)
            character_1.set_skill(character_1.get_skill() + skill_modifier)
            character_2.set_strength(character_2.get_strength() - strength_modifier)
            character_2.set_skill(character_2.get_skill() - skill_modifier)
        else:
            print "Player 2 wins!"
            character_1.set_strength(character_1.get_strength() - strength_modifier)
            character_1.set_skill(character_1.get_skill() - skill_modifier)
            character_2.set_strength(character_2.get_strength() + strength_modifier)
            character_2.set_skill(character_2.get_skill() + skill_modifier)


if __name__ == "__main__":
    characters = []
    characters.append(make_character_user_set_attribute_levels("Character 1"))
    characters.append(make_character_user_set_attribute_levels("Character 2")) 
    
    print_characters(characters)
    
    print "Let battle commence!"
    encounter(characters[0], characters[1])
    
    print_characters(characters)
