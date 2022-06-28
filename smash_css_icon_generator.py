import os

from PIL import Image

from smash_css_data_handler import Character

def getIcons(img_dir: os.PathLike, character_list: list[Character]) -> list[Image.Image]:
    img_list = []

    for character in character_list:
        file_name = character.name.replace("/"," ")
        img_list.append(Image.open(os.path.join(img_dir, file_name + ".png")))

    return img_list

def createImageGrid(imgs: list[Image.Image], rows: int, cols: int) -> list[Image.Image]:
    w, h = imgs[0].size
    grid = Image.new('RGBA', size=(cols*w, rows*h))
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))

    return grid