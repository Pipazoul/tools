# Based  lastfm exported songs creates a csv with all genres related to a track

# coding=utf-8
import os
import sys
from datetime import date
from datetime import datetime
from os import path
import csv
import discogs_client
import time
#reload(sys)
#sys.setdefaultencoding('utf-8')


file = "path/to/lastfm.csv"
year = 2019
filterByDate = False

lastfmDateFormat = [
    "%d %b %Y %H:%M",
    "%Y-%m-%dT%H:%M:%fZ"
]
d = discogs_client.Client('ExampleApplication/0.1', user_token="YourTokenHere")

notFound = 0

totalTracks = 0
nbStatus = 0
with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    #Count files
    for row in reader :
        date = row[3]
        try :
            parsedDate = datetime.strptime(date, lastfmDateFormat[0])
        except :
            print('Not formated well')
        if year == parsedDate.year or filterByDate == False:
            totalTracks = totalTracks + 1
    print('Total Tracks : '+str(totalTracks))
    time.sleep(5)
with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader :
        artist = row[0]
        album = row[1]
        title = row[2]
        date = row[3]
        try :
            parsedDate = datetime.strptime(date, lastfmDateFormat[0])
        except :
            print('Not formated well')
        if year == parsedDate.year or filterByDate == False:
            print('Artist : ' + artist + ' Album : ' + album + ' Title : ' + title + ' Date : ' + date)
            print('console 1')
            try :
                print('console 2')
                track = d.search(artist +' - '+ album + ' - ' + title, type='release')
                nbStatus = nbStatus + 1
                print(str(nbStatus) + '/' + str(totalTracks))
                print(track[0].styles)
                genres = ''
                print('console 3')
                for style in track[0].styles :
                    print('console 4')
                    genres = genres + ':' + style
                f=open('output/lastfm_'+str(year)+'.csv', 'a')
                f.write(artist + ',' + album + ',' + title + ',' + genres + ',' + date + '\n')
                print('console 4')
                print('Added genres to file')
                time.sleep(1)
            except :
                print('console 6')
                nbStatus = nbStatus + 1
                print(str(nbStatus) + '/' + str(totalTracks))
                notFound = notFound + 1
                print('No track found ' + str(notFound))
                f=open('output/lastfm_'+str(year)+'.csv', 'a')
                f.write(artist + ',' + album + ',' + title + ', undefined'+ ',' + date + '\n')
                print('Did not add genre to file')
                time.sleep(1)