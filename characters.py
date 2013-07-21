from rpg import make_character

characters = []
characters.append(make_character("Character 1"))
characters.append(make_character("Character 2"))

characters_file = open('characters.txt', 'w')

for character in characters:
    print>>characters_file, character
