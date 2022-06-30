import os

import tkinter as tk
from PIL import ImageTk

from smash_css_data_handler import TeamColor, generateCharacterData, loadCharacterData
from smash_css_icon_generator import loadImage, getIcons, createImageGrid, saveImageGrid

BUTTON_GRID_WIDTH = 13
ICON_GRID_WIDTH = 13

PORTRAIT_WIDTH = int(454/4)
PORTRAIT_HEIGHT = int(300/4)

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

def getColorCode(team: TeamColor) -> str:
    if (team == TeamColor.RED):
        return '#FF7F7F'
    elif (team == TeamColor.BLUE):
        return '#7F7FFF'
    elif (team == TeamColor.GREEN):
        return '#7FFF7F'
    elif (team == TeamColor.YELLOW):
        return '#FFFF7F'
    else:
        return 'SystemButtonFace'

class SmashCSS_GUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.onStartup()
        self.button_list = self.createButtons()

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

    def createButtons(self) -> list[tk.Button]:
        button_list = []

        for idx, c in enumerate(self.character_list):
            portrait = loadImage(self.getPath(CSS_PATH), c.name)
            portrait = portrait.resize((PORTRAIT_WIDTH,PORTRAIT_HEIGHT))
            portrait.show()
            portrait = ImageTk.PhotoImage(portrait)

            button = tk.Button(self, text=c.name, image=portrait, compound="top", foreground='black', background=getColorCode(c.team))
            button.grid(column=int(idx%BUTTON_GRID_WIDTH), row=int(idx/BUTTON_GRID_WIDTH))
            button_list.append(button)

        return button_list

    def getPath(self, path: str) -> os.PathLike:
        return os.path.join(self.dirname, path)

    def updateImages(self) -> None:
        for team_color in TeamColor:
            draw_list = [c for c in self.character_list if c.team == team_color]
            img_list = getIcons(self.getPath(ICON_PATH), draw_list)
            output = createImageGrid(img_list, int(len(img_list)/ICON_GRID_WIDTH) + 1, ICON_GRID_WIDTH)
            saveImageGrid(self.getPath(self.output_dirs[team_color.value]), output)