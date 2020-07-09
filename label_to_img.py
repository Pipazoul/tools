#Exports the annoted image from openImage Labeler annotations
# python label_to_img.py path/to/file
import os
import sys    
import time
import psutil
import shutil
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET
from PIL import Image
path = sys.argv[1]

resize = False
data_paths = [f for f in listdir(path) if isfile(join(path, f))]

print(sys.argv)


outNb = 0
print(data_paths)
for file in data_paths :
    try :
        print(file)
        filePath = path + '/' + file
        print(filePath)
        root = ET.parse(str(filePath)).getroot()
        #print(root)
        imgPath = root.find('path')
        imgPath = imgPath.text
        for item in root.findall('object'):
            coord = []
            print(item)

            bndbox = item.find('bndbox')
            for child in bndbox:
                print(child)
                #print(child.attrib['xmin'])
                coord.append(child.text)
            print(coord)
            xmin = int(coord[0])
            ymin = int(coord[1])
            xmax = int(coord[2])
            ymax = int(coord[3])

            x = (xmin,xmax)
            y = (ymin,ymax)
            im = Image.open(imgPath)
            im_crop = im.crop((xmin,ymin,xmax,ymax))
            im_crop.save(str(outNb)+'.jpg', quality=95)
            #crop_img = img[y:y+h, x:x+w]
            outNb = outNb + 1
    except :
        print('SOMETHING FAILED')
        time.sleep(2)
    #exit()