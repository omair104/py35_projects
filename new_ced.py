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
<<<<<<< HEAD
    extracted_path = r'F:\freelance work\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\extracted'
    cleaned_path = r'F:\freelance work\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\cleaned'
=======
    extracted_path = r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\extracted'
    cleaned_path = r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\cleaned'
    g=open(r'H:\circle\text_extractor\new corpus\CED\A Corpus of English Dialogues 1560-1760_ORIGINAL\2507\foreign2.txt', 'w')
>>>>>>> branch 'master' of https://github.com/omair104/py35_projects
    
    files= os.listdir(extracted_path)
    
    for filename in files:
        #file= 'D1MDANDO.txt'
        path_extracted_file= os.path.join(extracted_path, filename)
        
        
        with open(path_extracted_file, encoding='utf-8') as f:
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(filename))
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
            
            
            content[x] = re.sub('<FOREIGN', '<foreign', content[x])
            content[x] = re.sub('/FOREIGN', '/foreign', content[x])
            if '<foreign' in content[x]:
                total_foreign = content[x]
                while '/foreign>' not in content[x]:
                    total_foreign = total_foreign[:-1]+content[x+1]
                    content[x+1] = content[x][:-1]+content[x+1]
                    content[x] = re.sub('<FOREIGN', '<foreign', content[x])
                    content[x] = re.sub('/FOREIGN', '/foreign', content[x])
                    content[x+1] = re.sub('<FOREIGN', '<foreign', content[x+1])
                    content[x+1] = re.sub('/FOREIGN', '/foreign', content[x+1])
                    x=x+1
                
                #content[x] = content[x][:-1]+content[x+1]
                    
            '''
                foreign = re.findall('<foreign.*?foreign>', total_foreign)
                for fo in foreign:
                    g.write(filename)
                    g.write('\n')
                    g.write(fo[9:-10])
                    g.write('\n')
                    total_foreign = re.sub(re.escape(fo), '...', total_foreign)
                content[x] = total_foreign
            '''
                    
            content[x] = re.sub('<foreign>Asmoroth ascende, veni Asmoroth, Asmoroth veni.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS SECUNDUS, SCHAENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>De Arte Amandi</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Non oportet sapientem in aduersis dolore concidere</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Aduersis te proba, vt fortunam, cum necesse fuerit,patienter insultantem feras</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>In nomine Iesus vnde venis? E purgatorio</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Ex pura eleemosyna,</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Maius peccatum habes</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Claro micante Auro</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS PRIMUS, SCENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>SCENA SECUNDA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>SCENA TERTIA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>SCOENA QUARTA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS SECUNDUS. SCOENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>SCOENA SECUNDA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>SCENA TERTIA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Legere et non intelligere negligere est</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>In oreduorum aut trium testium peribit qui interficitur. Nemooccidatur uno contra se dicente testimonium.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Non stabit unus testis contra aliquem: quicquidillud peccati, et facinoris fuerit. Sed in ore duorum auttrium testium stabit omne verbum.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Nulli negabimus, nulli vendemus,nulli deferremus Justitiam</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Mi dispiace infinamente</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>interrumpato, gli Affari</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>una belissima Sorella in Verita`</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>O Cara Inghilterra</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Il nostro amico</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Il mio proprio Gusto</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>una Introduzione</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Senza Ceremonie</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Cosa e` questa -- Cosa, e`</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>O! Spiritoso Amico</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>il mio</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Conduttore` in tutte le Partite</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Multi ob stultitiam non putabant,multi ob ignorantiam non videbant, multi ob pravitatemnon credebant, &amp; non credendo conjurationem adjuvabant</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Quodnunquam de hoc facto animam in vita sua ipse purgaret.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Si steterit testis mendax contra hominem accusans cumprevaricatione, stabunt ambo, quorum causa est ante dominum, inconspectu sacerdotum, et judicum, qui fuerint in diebus illis</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Si judicaveritis tanquam jamjudicandi estis</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS SECUNDUS, SCHAENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS SECUNDUS, SCHAENA SECUNDA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS TERTIUS, SCHAENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS TERTIUS, SCAENA SECUNDA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS TERTIUS, SCHAENA TERTIA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS TERTIUS, SCHAENA QUARTA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS TERTIUS, SCHAENA QUINTA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUARTUS, SCHAENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUARTUS, SHAENA SECUNDA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUARTUS. SCHAENA TERTIA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUARTUS, SCHAENA QUARTA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUARTUS, SCHAENA QUINTA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUINTUS, SHAENA PRIMA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUINTUS, SCHAENA SECUNDA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUINTUS, SCHAENA TERTIA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>ACTUS QUINTUS, SCHAENA QUARTA.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Patresaequum esse censent nos iam iam a pueris illico nasci senes, neque illarum affines esse rerum, quas fert adolescentia</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Est modusin rebus sunt, certi denique fines</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>O tempora, O mores, O Poetarum flores</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Ambubaiarum collegia, pharmacapolae, mendici mimi balatrones, hoc genus omne.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Exercizo te Conjuro te in Nomine, &amp;c.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Je l\'escorche</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>O Cives, Cives, quaerunda, pecuniaprimum,Virtus post nummos</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Nec tam praesentes alibi cognoscere Divos</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Manemirer</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Fe, fe, fe, fe, mai foy, il fait for chando,   Ie man voi a leCourt la grand affaires.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Ouy mette le au mon</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>de-peech</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>que ay ieoublie</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>sed nunquampenetravit, quamvis inter femine, semen suum consumpsit</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Gratus mihi aduenis quid me cum vis.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Optatum venis paucis to volo.</foreign>', '...', content[x])
            content[x] = re.sub('<foreign>Si quid industria nostra tibi faciet dic      queso.</foreign>', '...', content[x])
            content[x] = re.sub('si mal-a proposito', '...', content[x])
            content[x] = re.sub('un Poco', '...', content[x])
            content[x] = re.sub('CUM PRIUILEGO', '...', content[x])
                    
            content[x] = re.sub('<foreign>', '', content[x])
            content[x] = re.sub('</foreign>', '', content[x])
                         
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
                
                content[x] = re.sub(re.escape('`'), '', content[x])
                
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