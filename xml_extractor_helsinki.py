import xml.etree.ElementTree as ET
path_to_xml=r'F:\freelance work\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\HC_XML_Master_v2.xml'
tree = ET.parse(path_to_xml)
root = tree.getroot()

print(root.tag)
print(root.attrib)
print(root.text)

#all_descendants = list(root.iter())
#print(all_descendants)
count =0
for node in  root.findall('TEI'):
    count = count +1

    print(node.text)
print(count)

    