# Image sorter
# creates folders based on users input tags and allows sorting the by using numpad
# Key 1 : tag1 Key2 : tag2 Key3 : other
# python tagger.py path/to/images
# creates folder in the images directory
import os
import sys    
from PIL import Image
import time
import psutil
import shutil
import keyboard
from os import listdir
from os.path import isfile, join
path = sys.argv[1]

resize = True
data_paths = [f for f in listdir(path) if isfile(join(path, f))]

print(sys.argv)
#query = sys.argv[2]
tag1 = input("Enter tag 1: ")
tag2 = input("Enter tag 2: ")
try :
    os.mkdir(path+'/' + tag1)
    os.mkdir(path+'/' + tag2)
    os.mkdir(path+'/' + 'other')

except :
    print('file already exists')


def CopyFile(tag,path, file):
    try :
        shutil.move(path + '/'+ file, path+'/'+ tag)
        print('file moved')
    except :
        print(file + 'Has maybe not be copied or is already here')

totalNb = 0
currentNb = 0
for file in data_paths :   
    totalNb = totalNb + 1

for file in data_paths :
    image = Image.open(path+'/'+file)
    try :
        width, height = image.size  
        if resize == True :
            size = (int(width/2),int(height/2))
            im1 = image.resize(size) 
            # Shows the image in image viewer  
            im1.show()
        else :  
            image.show()
    except :
        print("Image problem")
        exit()
        #time.sleep(0.4)
    a = keyboard.read_key()
    if a == '1' :
        print(tag1)
        CopyFile(tag1,path, file)
    elif a == '2':
        print(tag2)
        CopyFile(tag2,path, file)
    elif a == '3':
        print("other")
        CopyFile("other",path, file)
    elif a == 'q':
        exit()
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()
    currentNb = currentNb + 1
    print(str(currentNb) + ' / ' + str(totalNb))
    time.sleep(0.1)
    
