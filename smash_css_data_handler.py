import json
from enum import Enum

class TeamColor(Enum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4

class Character:
    def __init__(self, name: str, team: TeamColor) -> None:
        self.name = name
        self.team = team

    def changeTeams(self, team: TeamColor) -> None:
        self.team = team
    

def generateCharacterData(in_file: str, out_file: str) -> list[Character]:
    with open(in_file) as f:
        name_list = json.load(f)

    character_list = []

    for name in name_list:
        character_list.append(Character(name, TeamColor.NONE))

    with open(out_file, 'w') as f:
        json.dump(character_list, f, indent=2)


def loadCharacterData(filepath: str) -> list[Character]:
    with open(filepath) as f:
        character_list = json.load(f)

    return character_list