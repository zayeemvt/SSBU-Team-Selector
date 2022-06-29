import os

from smash_css_data_handler import TeamColor, generateCharacterData, loadCharacterData
from smash_css_icon_generator import getIcons, createImageGrid, saveImageGrid

GRID_WIDTH = 13

OUTPUT_DIR = "../Output/"

CHAR_NAME_PATH = "characters.json"
ICON_PATH = "../Images/Stock Icons/"
CSS_PATH = "../Images/CSS Portraits/"

CHAR_DATA_PATH = OUTPUT_DIR + "data.json"
RED_PATH = OUTPUT_DIR + "red_team.png"
BLUE_PATH = OUTPUT_DIR + "blue_team.png"
GREEN_PATH = OUTPUT_DIR + "green_team.png"
YELLOW_PATH = OUTPUT_DIR + "yellow_team.png"
NONE_PATH = OUTPUT_DIR + "no_team.png"

def getPath(path: str) -> os.PathLike:
    return os.path.join(dirname, path)

if __name__ == '__main__':
    print("Setting current working directory...")
    try:
        dirname = os.path.dirname(__file__)
        print("Current working directory has been set.")
    except Exception as e:
        print("Could not set current working directory.")
        print(type(e))
        quit()

    print("Creating output directory...")
    try:
        os.mkdir(getPath(OUTPUT_DIR))
        print("Output directory successfully created")
    except FileExistsError:
        print("Directory already exists.")
    except Exception as e:
        print("Failed to generate output directory.")
        print(type(e))
        quit()

    print("Loading save data...")
    try:
        character_list = loadCharacterData(getPath(CHAR_DATA_PATH))
        print("Saved data loaded.")
    except FileNotFoundError:
        character_list = generateCharacterData(getPath(CHAR_NAME_PATH), getPath(CHAR_DATA_PATH))
        print("Created new save data.")
    except Exception as e:
        print("Could not load save data.")
        print(type(e))
        quit()

    draw_list = [c for c in character_list if c.team is TeamColor.RED]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    output = createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH)
    saveImageGrid(getPath(RED_PATH), output)

    draw_list = [c for c in character_list if c.team is TeamColor.BLUE]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    output = createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH)
    saveImageGrid(getPath(BLUE_PATH), output)

    draw_list = [c for c in character_list if c.team is TeamColor.GREEN]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    output = createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH)
    saveImageGrid(getPath(GREEN_PATH), output)

    draw_list = [c for c in character_list if c.team is TeamColor.YELLOW]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    output = createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH)
    saveImageGrid(getPath(YELLOW_PATH), output)

    draw_list = [c for c in character_list if c.team is TeamColor.NONE]

    img_list = getIcons(getPath(ICON_PATH), draw_list)
    output = createImageGrid(img_list, int(len(img_list)/GRID_WIDTH) + 1, GRID_WIDTH)
    saveImageGrid(getPath(NONE_PATH), output)