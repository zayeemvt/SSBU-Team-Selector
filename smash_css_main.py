from smash_css_data_handler import loadCharacters
from smash_css_icon_generator import getIcons, createImageGrid

GRID_WIDTH = 13

if __name__ == '__main__':
    chars_filepath = "characters.json"

    character_list = loadCharacters(chars_filepath)

    # Iterating through the json
    # list
    for idx, name in enumerate(character_list, 1):
        print(str(idx) + ": " + name)

    img_list = getIcons(character_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()