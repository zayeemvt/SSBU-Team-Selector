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
    def __init__(self, name: str, team: TeamColor) -> None:
        self.name = name
        self.team = team

    def changeTeams(self, team: TeamColor) -> None:
        self.team = team
    

def saveCharacterData(filepath: os.PathLike, character_list: list[Character]) -> None:
    with open(filepath, 'w') as f:
        data = []

        for character in character_list:
            data.append({"name":character.name, "team": character.team.value})

        json.dump(data, f, indent=2, ensure_ascii=False)


def generateCharacterData(in_file: os.PathLike, out_file: os.PathLike) -> list[Character]:
    with open(in_file) as f:
        name_list = json.load(f)

    character_list = []

    for name in name_list:
        character_list.append(Character(name, TeamColor.NONE))

    saveCharacterData(out_file, character_list)

    return character_list


def loadCharacterData(filepath: str) -> list[Character]:
    with open(filepath) as f:
        data = json.load(f)

    character_list = []
    for character in data:
        character_list.append(Character(character["name"], character["team"]))

    return character_list