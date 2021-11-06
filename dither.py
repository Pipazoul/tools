import os
import sys    
import subprocess

print(sys.argv)
path = sys.argv[1]

palette = 'black white'


data_paths = [os.path.join(pth, f)
    for pth, dirs, files in os.walk(path) for f in files]



for file in data_paths :
    fileInfo =  file_extension = os.path.splitext(file)
    fileName = os.path.basename(file)
    filePath = file.replace(" ", "\ ")
    if fileInfo[1].lower() == ".png" or fileInfo[1].lower() == ".jpg" :
        try :
            print("didder --palette '"+palette+"' -i "+filePath+" -o "+filePath+" bayer 16x16 ")
            os.system("didder --palette '"+palette+"' -i "+filePath+" -o "+filePath+" bayer 16x16 ")
        except :
            print(file + 'Has maybe not be copied or is already here')
