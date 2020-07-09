#Generates a wordcloud based on text file
from os import path
import csv
import operator
import plotly.express as px
import matplotlib.pyplot as plotter

# Open the file in read mode 
text = open("pathToFile", "r") 
  
# Create an empty dictionary 
d = dict() 
totalWords = 0
# Loop through each line of the file 
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
  
    # Iterate over each word in line 
    for word in words: 
        if len(word) >= 5:
            # Check if the word is already in dictionary 
            if word in d: 
                # Increment count of word by 1 
                d[word] = d[word] + 1
            else: 
                # Add the word to dictionary with count 1 
                d[word] = 1
  
sorted_words = sorted(d.items(),reverse=True, key=operator.itemgetter(1))

i = 0
statNb = 5
while i < statNb :
    totalWords = totalWords + sorted_words[i][1]
    print(sorted_words[i])
    i = i+1

print('Total words : ' + str(totalWords))
# Get pourcentage
i = 0
#pieLabels = ()
populationShare = []
while i < statNb :
    percentage = float(sorted_words[i][1]) / totalWords * 100
    print(sorted_words[i][0] +' : ' + str(percentage) + '%')
    i = i+1
    #pieLabels = tuple(sorted_words[i][0])
    populationShare.append(percentage)

# TODO append the tuple variable pieLabel :)
# The slice names of a population distribution pie chart
pieLabels = 'label1', 'label2', 'label3', 'label4', 'label5'


figureObject, axesObject = plotter.subplots()

# Draw the pie chart

axesObject.pie(populationShare,

        labels=pieLabels,

        autopct='%1.2f',

        startangle=90)

 

# Aspect ratio - equal means pie is a circle

axesObject.axis('equal')

 

plotter.show()