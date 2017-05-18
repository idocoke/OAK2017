import os

images = os.listdir('JPEGImages')

for i,im in enumerate(images):
	inx = int(im.split('.')[0])
	os.rename('JPEGImages/'+im,'JPEGImages2/{}.jpg'.format(inx+1))
	os.rename('Annotations/'+im.split('.')[0]+'.xml','Annotations2/{}.xml'.format(inx+1))

