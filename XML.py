import xml.etree.ElementTree as ET
import sys

tree1 = ET.parse(sys.argv[1])
tree2 = ET.parse(sys.argv[2])


root1 = tree1.getroot()
root2 = tree2.getroot()

# At the very lowest level, dictionaries
# Create a list of lists
# 
for child in root1:
	print(child.tag, child.attrib)