#Gets search youtube search and view queries by parsing search.json export 
# coding=utf-8
import os
import json
import sys
import re 
from datetime import date
from datetime import datetime
from os import path
import validators
from wordcloud import WordCloud
reload(sys)
sys.setdefaultencoding('utf-8')

#TODO PARSE BY YEAR 

# Parsing method googleSearch / youtubeViews
parsingType = "youtubeViews"
file = "path/to/youtube_search.json"
year = 2019
json = json.loads(open(file).read())


googleDateFormats = [
    "%Y-%m-%dT%H:%M:%S.%fZ",
    "%Y-%m-%dT%H:%M:%fZ"
]

for search in json :
    title = search['title']
    date = search['time']
    #"time": "2020-01-04T14:52:12.292Z",
    try :
        parsedDate = datetime.strptime(date, googleDateFormats[0])
    except :
        try :
            parsedDate = datetime.strptime(date, googleDateFormats[1])
        except :
            print(date + " will not be used because the format is wrong")
    if parsingType == 'googleSearch' :
        if 'Vous avez recherch' in title :
            if parsedDate.year == year :
                print(parsedDate)
                parsedTitle = title.split('Vous avez recherché')
                f=open('output/research_'+str(year), 'a')
                f.write(parsedTitle[1]+ '\n')
    elif parsingType == "youtubeViews" :
        if 'Vous avez regard' in title :
            if parsedDate.year == year :
                print(parsedDate)
                parsedTitle = title.split('Vous avez regardé')
                parsedTitle = parsedTitle[1].split('- YouTube')
                print(parsedTitle[0])
                parsedTitle[0] = re.sub(r'http\S+', '', parsedTitle[0])
                f=open('output/youtubeViews_'+str(year), 'a')
                f.write(parsedTitle[0]+ '\n')



