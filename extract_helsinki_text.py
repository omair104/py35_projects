import os 
import re

def filter_text(org):
    result= org
    return result

path_to_xml=r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\HC_XML_Master_v2.xml'

'''
with open(path_to_xml, encoding='utf-8') as f:
    content = f.readlines()
    
for a in content:
    b= a.encode('utf-8')
    list.append(b)
count = 0
path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei'

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

path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'
file_number=0

extracted_tei = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei\428.txt'
extracted_tei_dir = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei'

files = os.listdir(extracted_tei_dir)
for file in files:
    extracted_tei2= os.path.join(extracted_tei_dir, file)
    print(extracted_tei2)
    
    with open(extracted_tei2, encoding='utf-8') as f:
        content = f.readlines()
        
    
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
    
    title_date=pubdate
    print(len(content))
    for x in range(0, len(content)):
        print(x)
        while ('<title level="m"' not in content[x]): 
            x=x+1
            if x==len(content):
                x=x-1
                break
        m = re.search("1", content[x])
        #print(m.start())
        
        if m:
            start= m.start()
            title_date= content[x][start:-9]
        break
    print(title_date)
    re.sub("[^123456789-]", '', title_date)
        
    opener_exists= False
    for x in range(0, len(content)):
        if ('<opener>' not in content[x]): 
            pass
        else:
            opener_exists= True
    
    
    
    x=0
    while ('<text' not in content[x]): 
            x=x+1        
     
    while(x<len(content)-2):
        file_number = file_number+1
        file= os.path.join(path, str(file_number)+'.txt')
        f= open(file, 'w+', encoding='utf-8')
        
    
        written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=helsinki_corpus_xml_edition> <title=%s> <author=%s> \
    <dialect=Early Modern English> <authorage=%s> <pubdate=%s> <genre1=let.non-priv> <genre2=X>  <encoding=utf-8> <text> \n\n' %(file_number,corpus_number, title, author, authorage, title_date)
    
        f.write(written_header)
        
        if opener_exists:
            while ('<opener>' not in content[x]): 
                x=x+1
                if x== len(content)-1:
                    break
            if x== len(content)-1:
                f.close()
                os.remove(file)
                file_number = file_number-1
                break
            while ('</opener>' not in content[x]): 
                res= filter_text(content[x])
                f.write(res[7:])
                x=x+1
            res= filter_text(content[x])
            f.write(res[7:])
            
    
    
        while ('<p>' not in content[x]): 
            x=x+1
            if x== len(content)-1:
                break
        if x== len(content)-1:
            f.close()
            os.remove(file)
            file_number = file_number-1
            break
        
        while ('</p>' not in content[x]): 
            res= filter_text(content[x])
            f.write(res[7:])
            x=x+1
        res= filter_text(content[x])
        f.write(res[7:])
        f.write('\n</text> </file>')
        x=x+1
    
    #print(written_header)
    
    f.close()
    
