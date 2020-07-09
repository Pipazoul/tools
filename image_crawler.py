# Script to get badly cached images on websites
# ex : mywebsite.com/cache/001.jpg  mywebsite.com/cache/002.jpg 
import urllib

i = 10020
max = 25000

while i < max :

	url = 'websiteUrl'+str(i)+'.f.jpg'
	urllib.urlretrieve(url, 'outputFolder/'+str(i) + ".jpg")
	print(url)
	i = i+1
	

