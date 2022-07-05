# SSBU Team Selector Tool
A Python 3.9.5 Tkinter application that generates image grids of character icons, sorted individually into teams based on the selections made in the GUI. This application is ideal for quickly displaying characters on a stream setup, as the output images can be added as sources in OBS or Streamlbas.

## Setup
### For users
Download the file as a .ZIP by clicking on the green "Code" button on GitHub and selecting "Download as ZIP". Once the download is complete, unzip the archive and place the folder in your desire location. The executable will be located in the `dist` folder. Run the `SSBU Team Selector.exe` file to launch the GUI. This will create an `Output` folder in the same directory as the executable.

### For developers
Clone the repository or create a fork. All source code is in the `src` directory. The `smash_css_main.py` file is the entry point into the application. All other files are supplementary to help modularize the code.

Modules used:
* PIL

## Using the Application
The team colors are as follows:
* Unselected
* Red
* Blue
* Green
* Yellow

Assign a team color for a character by clicking on its button. Right-clicking on the character cycles its color in the order listed above, while left-clicking goes in the opposite order.

The checkboxes at the bottom are used to select which team colors to generate images for. To ensure image generation is quick, please make sure any checkboxes with teams you don't want to generate images for are unchecked.

Click the "Update" button to generate the images. The generated images will be located in the `Output` folder, with the names `red_team.png`, `blue_team.png`, `green_team.png`, `yellow_team.png`, and `no_team.png` as applicable.

## Modifying the Application
The application data should be simple to modify without needing to change any of the code. If you would like to use this for anything else besides Smash Ultimate, you can swap out the images and character names.

The `characters.json` file has a list of all character names used in the application, in the order that they will appear in the GUI. If any characters have special characters (such as accented letters), you may have to use the Unicode value for that character instead to ensure that the program reads the name correctly.

All images used are stored in the `Images` directory. The `CSS Portraits` subdirectory is used for all of the images that appear on the GUI, whereas the `Stock Icons` subdirectory is used for the output images. Please ensure that all file names match the character names specified in `characters.json` with `.png` as the file extension. For any names with characters not allowed in file names, replace that character in the file name with a space (` `).

For developers, the executable and its respective directories were generated using the `auto-py-to-exe` GUI. In order to ensure the executable works properly, the following files and directories need to be included when running the `auto-py-to-exe` GUI:
* `Images`
* `characters.json`
* `smash_css_data_handler.py`
* `smash_css_gui.py`
* `smash_css_icon_generator.py`
