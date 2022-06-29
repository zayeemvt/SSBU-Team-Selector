import os

from smash_css_data_handler import TeamColor, generateCharacterData, loadCharacterData
from smash_css_icon_generator import getIcons, createImageGrid

GRID_WIDTH = 13

OUTPUT_DIR = "../Output/"

CHAR_NAME_PATH = "characters.json"
CHAR_DATA_PATH = OUTPUT_DIR + "data.json"
ICON_PATH = "../Images/Stock Icons/"

def getPath(path: str) -> os.PathLike:
    return os.path.join(dirname, path)

if __name__ == '__main__':
    print("Setting current working directory...")
    try:
        dirname = os.path.dirname(__file__)
        print("Current working directory has been set.")
    except:
        print("Could not set current working directory.")
        quit()

    print("Creating output directory...")
    try:
        os.mkdir(getPath(OUTPUT_DIR))
        print("Output directory successfully created")
    except FileExistsError:
        print("Directory already exists.")
    except FileNotFoundError:
        print("Failed to generate output directory.")
        quit()

    print("Loading save data...")
    try:
        character_list = loadCharacterData(getPath(CHAR_DATA_PATH))
        print("Saved data loaded.")
    except FileNotFoundError:
        character_list = generateCharacterData(getPath(CHAR_NAME_PATH), getPath(CHAR_DATA_PATH))
        print("Created new save data.")
    except:
        print("Could not create save data.")
        quit()

    draw_list = [c for c in character_list if c.team is TeamColor.RED.value]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()

    draw_list = [c for c in character_list if c.team is TeamColor.BLUE.value]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()

    draw_list = [c for c in character_list if c.team is TeamColor.GREEN.value]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()

    draw_list = [c for c in character_list if c.team is TeamColor.YELLOW.value]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()

    draw_list = [c for c in character_list if c.team is TeamColor.NONE.value]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH).show()