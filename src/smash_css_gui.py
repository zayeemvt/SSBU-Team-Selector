import os

import tkinter as tk
from PIL import Image, ImageTk

from smash_css_data_handler import Character, TeamColor, generateCharacterData, loadCharacterData, saveCharacterData
from smash_css_icon_generator import loadImage, getIcons, createImageGrid, saveImageGrid

# Constants
BUTTON_GRID_WIDTH = 13
ICON_GRID_WIDTH = 13

BUTTON_SPACING_X = 1
BUTTON_SPACING_Y = 1

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

DEFAULT_TEAMS = ["Red", "Blue"]

def getColorCode(team: TeamColor) -> str:
    """
    Translates a team color into the appropriate button color
    """

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

class Character_Button(tk.Label):
    """
    A wrapper class used to hold data for a character and provide
    an interface to change that character's team. Note that although
    the inherited class is "Label", this class is meant to functionally
    act as a button. However, the "Button" class has some limitations.
    """
    
    def __init__(self, root: tk.Frame, data: Character, idx: int, img: Image.Image) -> None:
        """
        Parameters:
        
        - root: The root component of the GUI, used to attach the buttons to the GUI
        - data: The Character class that this button will represent
        - idx:  Effectively an "ID number" for the button; used to sort it into the GUI
        - img:  The PIL image that will be displayed on the button
        """
        
        self.data = data

        # Convert image to be Tkinter-compatible
        self.portrait = img
        self.portrait = self.portrait.resize((PORTRAIT_WIDTH,PORTRAIT_HEIGHT))
        self.portrait = ImageTk.PhotoImage(self.portrait)

        # Create and place button
        super().__init__(root, text=data.name, image=self.portrait, compound="top", foreground='black', background=getColorCode(data.team), relief="solid")
        self.grid(column=int(idx%BUTTON_GRID_WIDTH), row=int(idx/BUTTON_GRID_WIDTH), padx=BUTTON_SPACING_X, pady=BUTTON_SPACING_Y)

        self.bind('<Button-1>', self.onLeftClick)
        self.bind('<Button-2>', self.onRightClick)
        self.bind('<Button-3>', self.onRightClick)

    def onLeftClick(self, event):
        """
        Cycle through team colors in ascending order.
        """
        
        new_team = (self.data.team.value + 1) % 5
        self.data.changeTeam(TeamColor(new_team))
        self.configure(background=getColorCode(self.data.team))

    def onRightClick(self, event):
        """
        Cycle through team colors in descending order.
        """

        new_team = (self.data.team.value + 4) % 5
        self.data.changeTeam(TeamColor(new_team))
        self.configure(background=getColorCode(self.data.team))



class SmashCSS_GUI(tk.Tk):
    """
    A wrapper class used to hold all data for the application, including its
    GUI components.
    """

    def __init__(self) -> None:
        super().__init__()
        self.onStartup()
        
        # Application title/header
        self.app_label = tk.Label(self, text="SSBU Team Selector Tool", font=("Helvetica", "32", "bold"), justify="center")
        self.app_label.grid(column=0, row=0)

        # Character buttons
        self.buttons_frame = tk.Frame(self)
        self.button_list = self.createButtons()
        self.buttons_frame.grid(column=0, row=1)

        # Team checkboxes
        self.check_frame = tk.Frame(self)
        self.check_list = self.createCheckboxes()
        self.check_frame.grid(column=0, row=2, pady=(5,5))

        # Update button
        self.update_btn = tk.Button(self, text="Update", command=self.saveData, padx=50, pady=10, font=("Helvetica", "16"), bd=5) 
        self.update_btn.grid(column=0, row=3, pady=(5,10))

        self.output_dirs = [NONE_PATH, RED_PATH, BLUE_PATH, GREEN_PATH, YELLOW_PATH]

    def onStartup(self) -> None:
        """
        Sets up and loads all directories and save data.
        """

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

        # For future development
        # Allow users to choose output directory
        # Make application remember output settings and checkbox values
        try:
            pass # load application settings
        except Exception as e:
            pass

    def createButtons(self) -> list[tk.Button]:
        """
        Generates all of the buttons for each character in the loaded character list
        """

        button_list = []

        for idx, c in enumerate(self.character_list):
            button = Character_Button(self.buttons_frame, c, idx, loadImage(self.getPath(CSS_PATH), c.name))
            button_list.append(button)

        return button_list

    def createCheckboxes(self) -> list[tk.Checkbutton]:
        """
        Generates the checkbox buttons used for selecting which team images to generate.
        """

        # Side label
        self.check_label = tk.Label(self.check_frame, text="Teams:", font=("Helvetica","12"))
        self.check_label.grid(column=0, row=0)

        button_list = []
        team_list = ["Unselected", "Red", "Blue", "Green", "Yellow"]
        self.check_vars = [tk.IntVar() for x in team_list] # Checkbox values for ease of access

        for idx, team in enumerate(team_list):
            button = tk.Checkbutton(self.check_frame, text=team, variable=self.check_vars[idx], font=("Helvetica","12"))
            if team in DEFAULT_TEAMS:
                button.select() # Sets some buttons as selected by default
            button.grid(column=idx+1, row=0)
            button_list.append(button)

        return button_list

    def getPath(self, path: str) -> os.PathLike:
        """
        Joins generic pathname to the current working directory path.
        Used for file access.
        """
        return os.path.join(self.dirname, path)

    def updateImages(self) -> None:
        """
        Generates and saves image grids of the characters selected in the
        GUI, based on their designated team and whether the team checkbox
        has been marked or not.
        """

        team_list = []

        # Decide which team images to generate
        for idx, v in enumerate(self.check_vars):
            if v.get() == 1:
                team_list.append(TeamColor(idx))

        for team_color in team_list:
            # Select characters only from the current team
            draw_list = [c for c in self.character_list if c.team == team_color]

            img_list = getIcons(self.getPath(ICON_PATH), draw_list)

            output = createImageGrid(img_list, int(len(img_list)/ICON_GRID_WIDTH) + 1, ICON_GRID_WIDTH)
            saveImageGrid(self.getPath(self.output_dirs[team_color.value]), output)

    def saveData(self) -> None:
        """
        Saves all character-related data, including the output image grids and
        the character data file.
        """

        for idx, c in enumerate(self.character_list):
            self.character_list[idx].team = self.button_list[idx].data.team

        self.updateImages()
        saveCharacterData(self.getPath(CHAR_DATA_PATH), self.character_list)