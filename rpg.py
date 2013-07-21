from random import randint
import math

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

def calculate_attribute_modifier(attribute, character1, character2):
    difference = abs(character1[attribute] - character2[attribute])
    
    modifier = math.floor(difference / 5)
    
    return modifier
# 
# def encounter(character1, character2):
#     strength_modifier = calculate_attribute_modifier('strength', character1, character2)
#     skill_modifier = calculate_attribute_modifier('skill', character1, character2)
#     
#     die_score1 = rand(1, 6)
#     die_score2 = rand(1, 6)
#     
#     if die_score1 != die_score2:
#         if die_score1 > die_score2:
#             character1[]
#         
    