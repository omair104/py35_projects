import os 


path_to_xml=r'F:\freelance work\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\HC_XML_Master_v2.xml'


with open(path_to_xml, encoding='utf-8') as f:
    content = f.readlines()
    
list=[]
for a in content:
    b= a.encode('utf-8')
    list.append(b)
count = 0
path = r'F:\freelance work\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'

for x in range(0, len(content)):
#for a in content:
    if '<text>' in content[x]:
        count = count +1
        file = os.path.join(path, str(count)+'.txt')
        f= open(file, 'w+', encoding='utf-8')
        y=x
        while('</text>' not in content[y]):
            f.write(content[y])
            y=y+1
        f.write(content[y])
