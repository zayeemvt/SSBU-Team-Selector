from PIL import Image

def getIcons(character_list: list[str]) -> list[Image.Image]:
    img_list = []

    for name in character_list:
        file_name = name.replace("/"," ")
        img_list.append(Image.open("Images/Stock Icons/" + file_name + '.png'))

    return img_list

def createImageGrid(imgs: list[Image.Image], rows: int, cols: int) -> list[Image.Image]:
    w, h = imgs[0].size
    grid = Image.new('RGBA', size=(cols*w, rows*h))
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))

    return grid