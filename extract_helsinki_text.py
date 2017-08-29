import os 
import re

path_to_xml=r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\HC_XML_Master_v2.xml'

'''
with open(path_to_xml, encoding='utf-8') as f:
    content = f.readlines()
    
for a in content:
    b= a.encode('utf-8')
    list.append(b)
count = 0
path = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei'

for x in range(0, len(content)):
#for a in content:
    if '<TEI ' in content[x]:
        count = count +1
        file = os.path.join(path, str(count)+'.txt')
        f= open(file, 'w+', encoding='utf-8')
        y=x
        while('</TEI>' not in content[y]):
            f.write(content[y][2:])
            y=y+1
        f.write(content[y][2:])


'''
extracted_tei = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei\428.txt'

with open(extracted_tei, encoding='utf-8') as f:
    content = f.readlines()
    
path = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'

    
tei= content[0]
n= re.findall('n=".*?"',tei)[0][3:-1]
id1 = re.findall('id=".*?"',tei)[0][4:-1]
corpus_number = n+'_'+id1

for x in range(0, len(content)):
    while ('<title key' not in content[x]): 
        x=x+1

    title= re.findall('n=".*?"',content[x])[0][3:-1]
    break

for x in range(0, len(content)):
    while ('<author key' not in content[x]): 
        x=x+1

    author= re.findall('key=".*?"',content[x])[0][5:-1]
    break

for x in range(0, len(content)):
    while ('author_age' not in content[x]): 
        x=x+1

    authorage= re.findall('target=".*?"',content[x])[0][13:-1]
    break

for x in range(0, len(content)):
    while ('<date type="manuscript"' not in content[x]): 
        x=x+1

    pubdate= re.findall('>.*?<',content[x])[0][1:-1]
    break

opener_exists= False
for x in range(0, len(content)):
    if ('<opener>' not in content[x]): 
        pass
    else:
        opener_exists= True

print(opener_exists)


file_number=0

x=0
while ('<text>' not in content[x]): 
        x=x+1        

while(x<len(content)-2):
    file= os.path.join(path, str(x)+'.txt')
    f= open(file, 'w+', encoding='utf-8')
    file_number = file_number+1

    written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=helsinki_corpus_xml_edition> <title=%s> <author=%s> \
<dialect=Early Modern English> <authorage=%s> <pubdate=%s> <genre1=let.non-priv> <genre2=X>  <encoding=utf-8> <text> \n\n' %(file_number,corpus_number, title, author, authorage, pubdate)

    f.write(written_header)
    
    if opener_exists:
        print('Do something here')
        while ('<opener>' not in content[x]): 
            x=x+1
            if x== len(content)-1:
                break
        if x== len(content)-1:
            f.close()
            os.remove(file)
            break
        while ('</opener>' not in content[x]): 
            f.write(content[x][7:])
            x=x+1
        f.write(content[x][7:])
        


    while ('<p>' not in content[x]): 
        x=x+1
        if x== len(content)-1:
            break
    if x== len(content)-1:
        f.close()
        os.remove(file)
        break
    
    print(x)
    while ('</p>' not in content[x]): 
        f.write(content[x][7:])
        x=x+1
    f.write(content[x][7:])
    f.write('\n</text> </file>')
print(len(content))
#print(written_header)

f.close()