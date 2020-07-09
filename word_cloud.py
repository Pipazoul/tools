# Generates a Worldcloud image based on a text file
import os
import json
import sys
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#image size
size = [1920, 1080]

# get file
text=open('path/to/myTextFile').read()
wordcloud = WordCloud(size[0], size[1]).generate(text)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud.png')
plt.show()
