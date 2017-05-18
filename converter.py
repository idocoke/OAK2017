import os
import Image

for im in os.listdir('JPEGImages'):
	image = Image.open('JPEGImages/'+im)
	image.save('JPEGImages2/'+im.split('.')[0]+'.jpg',"JPEG")
	print 'saved: '
	print im
