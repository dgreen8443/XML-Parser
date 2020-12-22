import xml.etree.ElementTree as ET
import sys

tree1 = ET.parse(sys.argv[1])
tree2 = ET.parse(sys.argv[2])


root1 = tree1.getroot()
root2 = tree2.getroot()

# At the very lowest level, dictionaries
# Create a master list with list if attribute has children, dictionary otherwise
# 
list1 = []
list2 = []
def depthCheck(attribute):
	if len(attribute) > 1:
		return 1
	else: 
		return 0

def rooting(attribute, lista):
	for child in attribute:
		if depthCheck(child) == 1:
			innerlist = []
			rooting(child, innerlist)
			lista.append(innerlist)
		else:
			tag = child.tag
			value = attribute.find(tag).text
			temp_dict = {tag : value}
			lista.append(temp_dict)
		
rooting(root1, list1)
print(list1)
print(list2)