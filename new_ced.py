import os,re

def extract():
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
            title= title.lower().capitalize()
            break
        
        for x in range(0, len(content)):
            while ('<author>' not in content[x]): 
                x=x+1
            author= re.findall('<author>.*?</author>',content[x])[0][8:-9]
            author = author.title()
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
        
        for x in range(0, len(content)):
            while ('<contemporaneity' not in content[x]): 
                x=x+1
            cont= re.findall('>.*?</contemporaneity>',content[x])[0][1:-18]
            break
        
        
        
        written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=corpus_of_english_dialogues_XML_edition> <title=%s> <author=%s> \
<pubdate=%s> <genre=%s> <encoding=utf-8> <notes=%s> <text> \n' %(file_number,filename, title, author, pubdate, genre, cont)
        
        
        
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


def markup():
    extracted_path = r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\extracted'
    cleaned_path = r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file, encoding='utf-8') as f:
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        while x< len(content):
            
            if '<comment' in content[x]:
                removes= re.findall('<comment.*?/comment>', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x])
                if removes == []:
                    while '/comment>' not in content[x]:
                        x=x+1
                    x=x+1


                
            if '<pagebreak' in content[x]:
                while '/>' not in content[x]:
                    x=x+1
                x=x+1
                
            elif '<sample' in content[x]:
                while '>' not in content[x]:
                    x=x+1
                x=x+1
                

                
            else:
                if x>1:
                    content[x] = re.sub('_', '', content[x])
                else:
                    content[x] = re.sub('unknown', 'X', content[x])
                content[x] = re.sub('&amp;', '&', content[x])
                content[x] = re.sub('&quot;', '', content[x])
                
                content[x] = re.sub('a~', 'ā', content[x])
                content[x] = re.sub('A~', 'Ā', content[x])
                content[x] = re.sub('e~', 'ē', content[x])
                content[x] = re.sub('E~', 'Ē', content[x])
                content[x] = re.sub('i~', 'ī', content[x])
                content[x] = re.sub('I~', 'Ī', content[x])
                content[x] = re.sub('o~', 'ō', content[x])
                content[x] = re.sub('O~', 'Ō', content[x])
                content[x] = re.sub('u~', 'ū', content[x])
                content[x] = re.sub('U~', 'Ū', content[x])
                content[x] = re.sub('v~', 'v̄', content[x])
                content[x] = re.sub('V~', 'V̄', content[x])
                content[x] = re.sub('y~', 'ȳ', content[x])
                content[x] = re.sub('Y~', 'Ȳ', content[x])
                content[x] = re.sub('m~', 'm̄', content[x])
                content[x] = re.sub('M~', 'M̄', content[x])
                content[x] = re.sub('p~', 'p̄', content[x])
                content[x] = re.sub('P~', 'P̄', content[x])

                
                content[x] = re.sub('<dialogueText>', '', content[x])
                content[x] = re.sub('</dialogueText>', '', content[x])
                content[x] = re.sub('<dialogue>', '', content[x])
                content[x] = re.sub('</dialogue>', '', content[x])
                content[x] = re.sub('<nonSpeech>', '', content[x])
                content[x] = re.sub('</nonSpeech>', '', content[x])
                content[x] = re.sub('<font>', '', content[x])
                content[x] = re.sub('</font>', '', content[x])
                content[x] = re.sub('<head>', '', content[x])
                content[x] = re.sub('</head>', '', content[x])
                content[x] = re.sub('<foreign>', '', content[x])
                content[x] = re.sub('</foreign>', '', content[x])
                content[x] = re.sub('</sample>', '', content[x])
                content[x] = re.sub('<emendation>', '', content[x])
                content[x] = re.sub('</emendation>', '', content[x])
                
                content[x] = re.sub('~', '', content[x])
                content[x] = re.sub('è', 'e', content[x])
                
                content[x] = re.sub('<omission type="line" />', '', content[x])
                content[x] = re.sub('<omission type="sentence" />', '', content[x])
                
                
                if x>1 and x!= len(content)-1 and '~' in content[x]:
                    print(file)
                    print(content[x])
                    break
                
                f.write(content[x])
                x=x+1
            
            
    
extract()
markup()