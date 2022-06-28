import os

from smash_css_data_handler import loadCharacterData
from smash_css_icon_generator import getIcons, createImageGrid

GRID_WIDTH = 13

CHAR_NAME_PATH = "characters.json"
CHAR_DATA_PATH = "data.json"
ICON_PATH = "Images/Stock Icons/"

if __name__ == '__main__':
    print("Setting current working directory...")
    try:
        dirname = os.path.dirname(__file__)
    except:
        print("Could not set current working directory")

    name_path = os.path.join(dirname, CHAR_NAME_PATH)
    character_list = loadCharacterData(name_path)

    for idx, name in enumerate(character_list, 1):
        print(str(idx) + ": " + name)

    icons_path = os.path.join(dirname, ICON_PATH)
    img_list = getIcons(icons_path, character_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()