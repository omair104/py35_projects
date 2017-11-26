import os,re

def extract():
    org_path = r'F:\freelance work\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\CEDXML'
    extracted_path = r'F:\freelance work\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\extracted'
    
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
        if author == 'Unknown' or author == '':
            author = 'X'
        
        for x in range(0, len(content)):
            while ('<speechPubDate>' not in content[x]): 
                x=x+1
            pubdate= re.findall('<speechPubDate>.*?</speechPubDate>',content[x])[0][15:-16]#[-4:]
            break
        pubdate = re.sub("[^0123456789]", '', pubdate)
        pubdate = pubdate[-4:]
        
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
        
        
        
        written_header = '<file> <no=%s> <filename=%s> <corpus=corpus_of_english_dialogues_XML_edition> <title=%s> <author=%s> \
<pubdate=%s> <genre=%s> <encoding=utf-8> <notes=%s> <text> \n' %(file_number,filename, title, author, pubdate, genre, cont)
        
        
        
        file= os.path.join(extracted_path, str(filename)+'.txt')
        f= open(file, 'w+', encoding='utf-8')
        f.write(written_header)
        f.write('\n')
        
        x=0
        while ('<frontMatter' not in content[x]): 
            x=x+1    
        print(x)        
         
        while(x<len(content)-1):        
            f.write(content[x])
            x=x+1
        f.write('\n</text> </file>')
        f.close


def markup():
    extracted_path = r'F:\freelance work\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\extracted'
    cleaned_path = r'F:\freelance work\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file, encoding='utf-8') as f:
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        while x< len(content)-1:
            
            if content[x].startswith('PP.'):
                x=x+1
                continue
                
            if '</frontMatter>' in content[x]:
                while '<dialogueText>' not in content[x]:
                    x=x+1
                x=x+1
                continue
                
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
            content[x] = re.sub('</sample>', '', content[x])
            content[x] = re.sub('<emendation>', '', content[x])
            content[x] = re.sub('</emendation>', '', content[x])
            content[x] = re.sub('<frontMatter>', '', content[x])
            content[x] = re.sub('</frontMatter>', '', content[x])
            content[x] = re.sub('</textBibliography>', '', content[x])
            content[x] = re.sub('</dialogueHeader>', '', content[x])
            
            if '<comment' in content[x] and 'comment>' not in content[x]:
                content[x+1]= content[x][:-1]+content[x+1]
                content[x+1]= re.sub('         ', '', content[x+1])
                x=x+1
                continue
            
            if content[x+1].startswith('<comment type="compiler">SOURCE TEXT:'):
                prev_word = content[x].split()[-1]
                content[x] = re.sub(re.escape(prev_word), '', content[x])
            
            
            if '<comment type="compiler">SOURCE TEXT:' in content[x] and '/comment>' in content[x]:
                comments = re.findall('<comment type="compiler">SOURCE TEXT:.*?/comment>', content[x])
                for a in comments:
                    comment = a 
                    #print('SOURCE:'+comment)
                    
                words = re.findall('SOURCE TEXT:.*?/comment>', content[x])
                for a in words:
                    word = a [12:-10]
                    #print('WORD:'+word)
                    
                previous = re.findall('^.*?<comment', content[x])
                #p = previous.split(' ')
                for p in previous:
                    list= p.split()
                    if len(list)>1:
                        last = list[-2]
                        #print('PREVIOUS: '+last)
                if previous == [] or previous == ['<comment']:
                    #last = content[x-1].split()[-1]
                    
                    content[x] = re.sub(re.escape(comment), '', content[x])
                    content[x] = word + content[x]
                    
                    
                        
                else:
                    content[x] = re.sub(re.escape(comment), '', content[x])
                    content[x] = re.sub(re.escape(last), word, content[x])
                #print('AFTER: '+ content[x])
            
            
            if '<comment' in content[x]:
                #print('ORIGINAL:'+content[x])
                removes= re.findall('<comment.*?/comment>', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x])
                if removes == []:
                    result = ''
                    while '/comment>' not in content[x]:
                        #print(content[x][:-2])
                        content[x]= content[x][:-2]
                        result = result+content[x]
                        x=x+1
                    result = result+content[x]
                    if not result.startswith('<comment'):
                        #print(file)
                        #print(result)
                        pass
                    c = re.findall('<comment.*?comment>', result)

                    content[x]= re.sub(re.escape(c[0]),'', result)
                    
                
            
            if '<foreign' in content[x]:
                    
                foreign = re.findall('<foreign.*?foreign>', content[x])
                for fo in foreign:
                    content[x] = re.sub(re.escape(fo), '...', content[x])
                    
                if foreign== []:
                    foreign_start = re.findall('<foreign.*?\n', content[x])
                    for fo in foreign_start:
                        content[x] = re.sub(re.escape(fo), '...', content[x])
                    
                    while 'foreign' not in content[x]:
                        x=x+1
                    #print(file)
                    #print(content[x])
                    content[x] = content[x].split('</foreign>')[1]
                    
                    '''
                    if 'FOREIGN' in content[x+1]:
                        content[x+1] = content[x+1].split('</FOREIGN>')[1]
                    else:
                        content[x+1] = re.sub('<foreign', '<FOREIGN', content[x+1])
                        content[x+1] = re.sub('/foreign', '/FOREIGN', content[x+1])
                        x=x+1
                        content[x+1] = re.sub('<foreign', '<FOREIGN', content[x+1])
                        content[x+1] = re.sub('/foreign', '/FOREIGN', content[x+1])
                    
                        print(file)
                        print(content[x])
                        print(content[x+1])
                        content[x+1] = content[x+1].split('</FOREIGN>')[1]
                    '''
                

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

                
                
                content[x] = re.sub('~', '', content[x])
                content[x] = re.sub('è', 'e', content[x])
                
                content[x] = re.sub('<omission type="line" />', '', content[x])
                content[x] = re.sub('<omission type="sentence" />', '', content[x])
                
                
                if x>1 and x!= len(content)-1 and '<foreign' in content[x]:
                    print(file)
                    print(content[x])
                    #break
                
                f.write(content[x])
                x=x+1

                
        f.write('\n</text> </file>')
            
            
    
#extract()
markup()