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
def depthCheck(element):
	if len(element) >= 1:
		return 1
	else: 
		return 0


	

def rooting(element, lista):
	print("$" + element.tag)
	
	lista.append(element.tag)
	for child in element:
		
		tag = child.tag
		att = child.attrib
	
		if depthCheck(child) == 1:
			
			rooting(child, lista)
			
		
		else:
			
			lista.append(tag)
			lista.append(att)
		


rooting(root1, list1)
rooting(root2, list2)
print(root1.tag	)
print(list1)
print()
print(list2)

diff1 = [x for x in list1 if x not in list2]
diff2 = [x for x in list2 if x not in list1]

print("\n\nIn list 1 not in list 2" )
print(diff1)
print("\n\nIn list 2 not in list 1" )
print(diff2)