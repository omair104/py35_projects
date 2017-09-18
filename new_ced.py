import os,re

org_path = r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\CEDXML'
extracted_path = r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\extracted'

files = os.listdir(org_path)
#print(files)
file_number=0
for file in files:
    file_number= file_number+1
    path_org_file= os.path.join(org_path, file)
    
    print(path_org_file)
    
    with open(path_org_file) as f:
        content = f.readlines()
        
    for x in range(0, len(content)):
        while ('<filename>' not in content[x]): 
            x=x+1
        filename= re.findall('<filename>.*?</filename>',content[x])[0][10:-11]
        break
    
    for x in range(0, len(content)):
        while ('<title>' not in content[x]): 
            x=x+1
        title= re.findall('<title>.*?</title>',content[x])[0][7:-8]
        break
    
    for x in range(0, len(content)):
        while ('<author>' not in content[x]): 
            x=x+1
        author= re.findall('<author>.*?</author>',content[x])[0][8:-9]
        break
    
    for x in range(0, len(content)):
        while ('<speechPubDate>' not in content[x]): 
            x=x+1
        pubdate= re.findall('<speechPubDate>.*?</speechPubDate>',content[x])[0][15:-16][-4:]
        break
    
    for x in range(0, len(content)):
        while ('<textType' not in content[x]): 
            x=x+1
        genre= re.findall('>.*?</textType>',content[x])[0][1:-11]
        break
    
    
    
    written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=corpus_of_english_dialogues_XML_edition> <title=%s> <author=%s> \
    <dialect=Early Modern English> <authorage=X> <pubdate=%s> <genre1=%s> <genre2=X>  <encoding=utf-8> <text> \n' %(file_number,filename, title, author, pubdate, genre)
    
    
    
    file= os.path.join(extracted_path, str(filename)+'.txt')
    f= open(file, 'w+', encoding='utf-8')
    f.write(written_header)
    
    x=0
    while ('<dialogueText' not in content[x]): 
        x=x+1    
    print(x)        
     
    while(x<len(content)-1):        
        f.write(content[x])
        x=x+1
    f.write('\n</text> </file>')
    f.close
