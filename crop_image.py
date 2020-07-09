# Initial code from Memo Akten 
# https://github.com/memo
# Crops batch of images into desired resolution
from PIL import Image
import os.path, sys


path = "1-input"
dirs = os.listdir(path)



i = 0

def imageCropper(fullpath, name):


    image  = Image.open(fullpath)
    width  = image.size[0]
    height = image.size[1]

    aspect = width / float(height)

    ideal_width = 200
    ideal_height = 200

    ideal_aspect = ideal_width / float(ideal_height)

    if aspect > ideal_aspect:
        # Then crop the left and right edges:
        new_width = int(ideal_aspect * height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
    else:
        # ... crop the top and bottom:
        new_height = int(width / ideal_aspect)
        offset = (height - new_height) / 2
        resize = (0, offset, width, height - offset)

    thumb = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)

    fill_color = '#FFFFFF'  # your background
    if image.mode in ('RGBA', 'LA'):
        background = Image.new(thumb.mode[:-1], thumb.size, fill_color)
        background.paste(thumb, thumb.split()[-1])
        thumb = background
    #im.save(hidpi_path, file_type, quality=95)
    


	
    thumb.save('../2-process/{}.jpg'.format(i))
    print(i)



for item in sorted(dirs):
    fullpath = os.path.join(path,item)         #corrected
    if os.path.isfile(fullpath):
        try:
            imageCropper(fullpath, i)
            print(os.path.basename(fullpath))
        except Exception:
            pass 

    i = i+1


