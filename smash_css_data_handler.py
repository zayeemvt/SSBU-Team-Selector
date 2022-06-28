import json

def loadCharacters(filepath: str) -> list[str]:
    # Opening JSON file
    f = open('characters.json')
    
    # returns JSON object as 
    # a dictionary
    character_list = json.load(f)

    # Closing file
    f.close()

    return character_list