# COMP 163 - Project 1: Character Creator & Chronicles

Author: Marcellus Hutchins  
Date: 10/27/25  




 Features

- Create new characters with customizable names and classes  
- Automatically calculate base stats by class  
- Save and load character data from text files  
- Level up characters with stat scaling based on class 
- Display full character information in a clean format
- Save displayed character in file.txt 
- Load character based on preexisting files 



Character Classes

| Class   | Strength | Magic | Health | Description |
| Warrior | High | Low | High | Strong fighters with great endurance |
| Mage| Low | High | Medium | Powerful spellcasters with fragile bodies |
| Rogue | Medium | Medium | Low | Agile adventurers with balanced stats |
| Cleric | Medium | High | High | Holy healers with balanced strength |

---

Functions Overview

create_character(name, character_class)
    - Creates a new character dictionary with base stats 

calculate_stats(character_class, level)
    -Calculates stats based on class and level 

save_character(character, filename)
    -Saves character data to a file  

load_character(filename)
    -Loads character data from a saved file 

display_character(character)
    -Prints formatted character details 

level_up(character)
    -Increases the character's level and scales stats |


