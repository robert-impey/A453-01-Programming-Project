from math import floor

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


def calculate_attribute_modifier(attribute, character1, character2):
    difference = abs(character1[attribute] - character2[attribute])
    
    modifier = floor(difference / 5)
    
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
    