from rpg import make_character

characters = []
characters.append(make_character("Character 1"))
characters.append(make_character("Character 2"))

characters_file = open('characters.txt', 'w')

if __name__ == "__main__":
    print >>characters_file, characters
