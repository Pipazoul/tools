# Based on a subtree of folders compresses video to mp4 
# Creates a backup of all the videos before compression

import os
import sys    
import subprocess
import ffmpeg
import shutil

print(sys.argv)
path = sys.argv[1]

# TODO add comparaison before after
# Create backup folder in folder

data_paths = [os.path.join(pth, f)
    for pth, dirs, files in os.walk(path) for f in files]

# Create backup dir
try :
    os.mkdir(path+'/backup')
except :
    print('file already exists')



for file in data_paths :
    fileInfo =  file_extension = os.path.splitext(file)
    fileName = os.path.basename(file)
    if fileInfo[1].lower() == ".mov" :
        try :
            shutil.copy(file, path+'/backup')
        except :
            print(file + 'Has maybe not be copied or is already here')

for file in data_paths :
    fileInfo =  file_extension = os.path.splitext(file)
    fileName = os.path.basename(file)
    if fileInfo[1].lower() == ".mov" :
        stream = ffmpeg.input(file)
        stream = ffmpeg.output(stream, os.path.dirname(file)+'/'+fileName.split('.')[0]+'.mp4',f='mp4', preset="ultrafast",crf=20, coder=1, pix_fmt="yuv420p")
        ffmpeg.run(stream)
        os.remove(file)
        print(os.path.dirname(file))