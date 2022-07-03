import os

import json
from enum import Enum

class TeamColor(Enum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4

class Character:
    """
    A class that represents a selectable character
    """

    def __init__(self, name: str, team: TeamColor) -> None:
        self.name = name
        self.team = team

    def changeTeam(self, team: TeamColor) -> None:
        self.team = team
    

def saveCharacterData(out_file: os.PathLike, character_list: list[Character]) -> None:
    """
    Saves the state of the application in the JSON file specified by out_file.
    """

    with open(out_file, 'w') as f:
        data = []

        # Convert to array of key-value pairs
        for character in character_list:
            data.append({"name":character.name, "team": character.team.value})

        json.dump(data, f, indent=2, ensure_ascii=False)


def generateCharacterData(in_file: os.PathLike, out_file: os.PathLike) -> list[Character]:
    """
    Makes a new JSON file with character data (specified by out_file), using the list
    of names from the JSON file specified by in_file.
    """

    # Fetch character names
    with open(in_file) as f:
        name_list = json.load(f)

    character_list = []

    # Initialize characters with default settings
    for name in name_list:
        character_list.append(Character(name, TeamColor.NONE))

    saveCharacterData(out_file, character_list)

    return character_list


def loadCharacterData(in_file: str) -> list[Character]:
    """
    Loads previously saved data from the JSON file specified by in_file.
    """
    
    with open(in_file) as f:
        data = json.load(f)

    character_list = []
    for character in data:
        character_list.append(Character(character["name"], TeamColor(character["team"])))

    return character_list