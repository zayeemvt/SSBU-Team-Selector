import os

from PIL import Image

from smash_css_data_handler import Character

def replaceSpecialChars(file_name: str) -> str:
    """
    Replaces any special characters in the character file_name with a file-name-
    compatible character.
    """
    special_chars = ["\\", "/", ":", "*", "?", "<", ">", "|"]
    for char in special_chars:
        file_name = file_name.replace(char," ")
    
    return file_name

def loadImage(img_dir: os.PathLike, file_name: str) -> Image.Image:
    """
    Returns a PIL image of the desired file_name in the specified img_dir path,
    in PNG format.
    """

    file_name = replaceSpecialChars(file_name)
    return Image.open(os.path.join(img_dir, file_name + ".png"))

def getIcons(img_dir: os.PathLike, character_list: list[Character]) -> list[Image.Image]:
    """
    Generates a list of output images from the specified character_list. These
    images will be retrieved from the path specified by img_dir, and the image
    files follow the format "Character Name.png". Any character names with
    special characters that can't be used in file names will have that special
    character replaced by a blank space.
    """

    img_list = []

    for character in character_list:
        img_list.append(loadImage(img_dir, character.name))

    return img_list

def createImageGrid(imgs: list[Image.Image], rows: int, cols: int) -> list[Image.Image]:
    """
    Creates a grid of output images specified by imgs, with dimensions cols * rows.
    Each image must have equal dimensions for best results.
    """

    # Get the image size in pixels
    if (len(imgs) != 0):
        w, h = imgs[0].size
    else:
        # Arbitrary numbers, since the output image will be blank anyway
        w = 64
        h = 64
    grid = Image.new('RGBA', size=(cols*w, rows*h))
    
    if (w > 0 and h > 0):
        for i, img in enumerate(imgs):
            grid.paste(img, box=(i%cols*w, i//cols*h))

    return grid

def saveImageGrid(out_file: os.PathLike, grid: list[Image.Image]) -> None:
    """
    Saves grid of images at specified out_file location.
    """

    grid.save(out_file)
    return