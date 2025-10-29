"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Marcellus Hutchins
Date: 10/27/25

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class,):
    if character_class == 'Warrior':
        character = {'name' : name,
        'class' : character_class,
        'level' : 1,
        'health' : 100,
        'gold' : 100,
        'strength' : 10,
        'magic' : 2}
    elif character_class == 'Mage':
        character = {'name' : name,
        'class' : character_class,
        'level' : 1,
        'health' : 60,
        'gold' : 100,
        'strength' : 3,
        'magic' : 10}
    elif character_class == 'Rogues':
        character = {'name' : name,
        'class' : character_class,
        'level' : 1,
        'health' : 30,
        'gold' : 100,
        'strength' : 6,
        'magic' : 5}
    elif character_class == 'Clerics':
        character = {'name' : name,
        'class' : character_class,
        'level' : 1,
        'health' : 90,
        'gold' : 100,
        'strength' : 6,
        'magic' : 8}
    return character

    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass
def calculate_stats(character_class, level, character=None):
    for level in range(level):
        if character_class == 'Warrior':
            character['strength'] *= 1.75
            character['magic'] += 1
            character['health'] += 20
        elif character_class == 'Mage':
            character['strength'] += 3
            character['magic'] *= 1.75
            character['health'] += 8
        elif character_class == 'Rogues':
            character['strength'] *= 1.20
            character['magic'] *= 1.15
            character['health'] += 5
    lvl_stat = (character['strength'], character['magic'], character['health'])
    return lvl_stat


    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    with open(filename, 'w') as f:
        f.write(f'Character Name: {character["name"]}')
        f.write(f'Class: {str(character["class"])}')
        f.write(f'Level: {str(character["level"])}')
        f.write(f'Strength: {str(character["strength"])}')
        f.write(f'Magic: {str(character["magic"])}')
        f.write(f'Health: {str(character["health"])}')
        f.write(f'Gold: {str(character["gold"])}')
    with open(filename, 'r') as f:
        character_data = f.read()
    return character_data

    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    if filename is None:
        print('None')
    else:
        print(filename)
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

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
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    level = character['level'] + 1
    calculate_stats(character, level)
    return None
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")
