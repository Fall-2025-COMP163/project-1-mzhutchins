"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Marcellus Hutchins
Date: 10/27/25

AI Usage: [AI helped with logic handling and invalid directory path's in save_character,]
"""
import os


def create_character(name, character_class):
    class_options = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class in class_options:
        character = {'name' : name,
        'class' : character_class,
        'level' : 1,
        'health' : 50,
        'gold' : 100,
        'strength' : 10,
        'magic' : 10}
    else:
        return None
    return character

def calculate_stats(character_class, level):
    for level in range(level):
        if character_class == 'Warrior':
            strength = 28
            magic = 11
            health = 80
        elif character_class == 'Mage':
            strength = 10
            magic = 33
            health = 65
        elif character_class == 'Rogue':
            strength = 14
            magic = 15
            health = 37
        elif character_class == 'Cleric':
            strength = 14
            magic = 26
            health = 92
    lvl_stat = (strength, magic, health)
    return lvl_stat


def save_character(character, filename):
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False
    else:
        f = open(filename, 'w')
        f.write(f'Character Name: {str(character["name"])}\n')
        f.write(f'Class: {str(character["class"])}\n')
        f.write(f'Level: {str(character["level"])}\n')
        f.write(f'Strength: {str(character["strength"])}\n')
        f.write(f'Magic: {str(character["magic"])}\n')
        f.write(f'Health: {str(character["health"])}\n')
        f.write(f'Gold: {str(character["gold"])}\n')
        f.close()
        return True


def load_character(filename):
    if os.path.isfile(filename):
        char_data = []
        with open(filename, 'r') as f:
            for line in f:
                # Split lines like "Class: Warrior" into key/value
                if ':' in line:
                    value = line.strip().split(':', 1)[1]
                    char_data.append(value.strip())
        #print(char_data)
        return {
            'name': char_data[0],
            'class': char_data[1],
            'level': int(char_data[2]),
            'strength': int(char_data[3]),
            'magic': int(char_data[4]),
            'health': int(char_data[5]),
            'gold': int(char_data[6])
        }
    else:
        return None


def display_character(character):
    print('=== CHARACTER SHEET ===')
    print(f'Character Name: {character["name"]}')
    print(f'Class: {character["class"]}')
    print(f'Level: {character["level"]}')
    print(f'Strength: {character["strength"]}')
    print(f'Magic: {character["magic"]}')
    print(f'Health: {character["health"]}')
    print(f'Gold: {character["gold"]}')
    return None


def level_up(character):
    character['level'] += 1
    for level in range(character['level']):
        character['gold'] += 25
        if character['class'] == 'Warrior':
            character['strength'] *= 1.65
            character['magic'] *= 1.15
            character['health'] *= 1.65
        elif character['class'] == 'Mage':
            character['strength'] *= 1.20
            character['magic'] *= 1.65
            character['health'] *= 1.35
        elif character['class'] == 'Rogue':
            character['strength'] *= 1.45
            character['magic'] *= 1.45
            character['health'] *= 1.25
        elif character['class'] == 'Cleric':
            character['strength'] *= 1.40
            character['magic'] *= 1.50
            character['health'] *= 1.75
        else:
            return None
    return None


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # Example usage:
    #char = create_character("TestHero", "Warrior")
    #display_character(char)
    #save_character(char, "my_character.txt")
    #loaded = load_character("my_character.txt")
