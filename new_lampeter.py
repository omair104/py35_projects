import os,re

org_path = r'H:\circle\text_extractor\new corpus\Lampeter\The Lampeter Corpus of Early Modern Tracts original\2400\Texts'
extracted_path = r'H:\circle\text_extractor\new corpus\Lampeter\The Lampeter Corpus of Early Modern Tracts original\2400\extracted'

files = os.listdir(org_path)
#print(files)
file_number=0
for file in files:
    file_number= file_number+1
    path_org_file= os.path.join(org_path, file)
    
    print(path_org_file)
    
    with open(path_org_file) as f:
        content = f.readlines()
    
    '''
    for x in range(0, len(content)):
        while ('<filename>' not in content[x]): 
            x=x+1
        filename= re.findall('<filename>.*?</filename>',content[x])[0][10:-11]
        break
    '''
    filename= file[:-4]
    
    for x in range(0, len(content)):
        while ('<TITLESTMT>' not in content[x]): 
            x=x+1
        title= re.findall(':.*?</TITLE>',content[x])[0][1:-8]
        break
    
    for x in range(0, len(content)):
        while ('<PERSNAME>' not in content[x]): 
            x=x+1
            if x  == len(content): 
                break
        if x<len(content):
            author= re.findall('<PERSNAME>.*?</PERSNAME>',content[x])[0][10:-11]
        else: author= ''
        break
    
    for x in range(0, len(content)):
        while ('<PUBPLACE>' not in content[x]): 
            x=x+1
            if x  == len(content): 
                break
        if x<len(content):
            pubplace = re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
        else: pubplace= ''
        break
    
    for x in range(0, len(content)):
        while ('<BOOKSELLER>' not in content[x]): 
            x=x+1
            if x  == len(content): 
                break
        if x<len(content):
            bookseller= re.findall('<BOOKSELLER>.*?</BOOKSELLER>',content[x])[0][12:-13]
        else: bookseller= ''
        break
    
    for x in range(0, len(content)):
        while ('<IDNO TYPE="Wing">' not in content[x]): 
            x=x+1
            if x  == len(content): 
                break
        if x<len(content):
            idno_wing= re.findall('<IDNO TYPE="Wing">.*?</IDNO>',content[x])[0][18:-7]
        else: idno_wing= ''
        break
    
    for x in range(0, len(content)):
        while ('<IDNO TYPE="Lamp">' not in content[x]): 
            x=x+1
            if x  == len(content): 
                break
        if x<len(content):
            idno_lamp= re.findall('<IDNO TYPE="Lamp">.*?</IDNO>',content[x])[0][18:-7]
        else: idno_lamp= ''
        break
    
    print(idno_wing)
    print(idno_lamp)
    
    for x in range(0, len(content)):
        while ('<DATE>' not in content[x]): 
            x=x+1
        pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
        break
    
    for x in range(0, len(content)):
        while ('<CATREF' not in content[x]): 
            x=x+1
        genre= re.findall('TARGET=.*?">',content[x])[0][8:-1]
        break
    
    genre1_a= genre[0:4]
    genre2_a= re.findall('\s.*?\s', genre)[0][1:-1]
    
    options = {'dom1' : 'economy',
           'dom2' : 'law',
           'dom3' : 'miscellaneous',
           'dom4' : 'politics',
           'dom5' : 'religion',
           'dom6' : 'science',}
    genre1 =options[genre1_a]
    
    options2={
    'ec1' : 'domestic economy and trade',
    'ec2' : 'foreign and colonial economy and trade',
    'ec3' : 'financial',
    'sci1' : 'medicine',
     'sci2' : 'geography',
     'sci3' : 'science other', 
     'law1' : 'specific case discussion', 
     'law2' : 'court records', 
     'law3' : 'administration', 
     'msc1' : 'biographical', 
     'msc2' : 'current interest', 
     'msc3' : 'practical application or advice'
    }
    genre2= options2.get(genre2_a, '')
    
    written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=lampeter_corpus> <title=%s> <author=%s> <authorage=unknown>\
<pubdate=%s> <genre1=tract, %s> <genre2=tract, %s> <place_of_publication=%s> <publisher=%s> <encoding=utf-8> \
<idno: Wing %s> <idno: Lamp %s> <text> \n' %(file_number,filename, title, author, pubdate, genre1, genre2, pubplace, bookseller, idno_wing, idno_lamp)
    
    print(written_header)
    
    file= os.path.join(extracted_path, str(filename)+'.txt')
    f= open(file, 'w+', encoding='utf-8')
    f.write(written_header)
    
    x=0
    while ('</TEIHEADER' not in content[x]): 
        x=x+1        
    x=x+1
    while(x<len(content)-1):  
        x=x+1      
        f.write(content[x])
    f.write('\n</text> </file>')
    f.close
    