import xml.etree.ElementTree as ET
import os

for xm in os.listdir('Annotations'):
	tree = ET.parse('Annotations/'+xm)
	root = tree.getroot()
	for targets in root.iter('xmin'):
		print targets.text
		targets.text = str(int(targets.text)+1)
		print targets.text
	for targets in root.iter('ymin'):
		print targets.text
		targets.text = str(int(targets.text)+1)
		print targets.text
	for targets in root.iter('xmax'):
		print targets.text
		targets.text = str(int(targets.text)+1)
		print targets.text
	for targets in root.iter('ymax'):
		print targets.text
		targets.text = str(int(targets.text)+1)
		print targets.text
	tree.write('Annotations/'+xm)
