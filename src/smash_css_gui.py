import os

from tkinter import *
from tkinter.ttk import *

from smash_css_data_handler import TeamColor, generateCharacterData, loadCharacterData
from smash_css_icon_generator import getIcons, createImageGrid, saveImageGrid

ICON_GRID_WIDTH = 13

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

class SmashCSS_GUI(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.onStartup()
        self.output_dirs = [NONE_PATH, RED_PATH, BLUE_PATH, GREEN_PATH, YELLOW_PATH]
        self.updateImages()

    def onStartup(self) -> None:
        print("Setting current working directory...")
        try:
            self.dirname = os.path.dirname(__file__)
            print("Current working directory has been set.")
        except Exception as e:
            print("Could not set current working directory.")
            print(type(e))
            quit()

        print("Creating output directory...")
        try:
            os.mkdir(self.getPath(OUTPUT_DIR))
            print("Output directory successfully created")
        except FileExistsError:
            print("Directory already exists.")
        except Exception as e:
            print("Failed to generate output directory.")
            print(type(e))
            quit()

        print("Loading save data...")
        try:
            self.character_list = loadCharacterData(self.getPath(CHAR_DATA_PATH))
            print("Saved data loaded.")
        except FileNotFoundError:
            self.character_list = generateCharacterData(self.getPath(CHAR_NAME_PATH), self.getPath(CHAR_DATA_PATH))
            print("Created new save data.")
        except Exception as e:
            print("Could not load save data.")
            print(type(e))
            quit()

        try:
            pass # load application settings
        except Exception as e:
            pass

    def getPath(self, path: str) -> os.PathLike:
        return os.path.join(self.dirname, path)

    def updateImages(self):
        for team_color in TeamColor:
            draw_list = [c for c in self.character_list if c.team == team_color]
            img_list = getIcons(self.getPath(ICON_PATH), draw_list)
            output = createImageGrid(img_list, int(len(img_list)/ICON_GRID_WIDTH) + 1, ICON_GRID_WIDTH)
            saveImageGrid(self.getPath(self.output_dirs[team_color.value]), output)