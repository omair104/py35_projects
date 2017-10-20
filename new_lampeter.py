import os,re

def extract():
    org_path = r'H:\circle\py\new corpus\Lampeter\The Lampeter Corpus of Early Modern Tracts original\2400\Texts'
    extracted_path = r'H:\circle\py\new corpus\Lampeter\The Lampeter Corpus of Early Modern Tracts original\2400\extracted'
    
    files = os.listdir(org_path)
    #print(files)
    file_number=0
    for file in files:
        file_number= file_number+1
        path_org_file= os.path.join(org_path, file)
        
        print(path_org_file)
        
        with open(path_org_file) as f:
            content = f.readlines()
        

        filename= file[:-4]
        
        for x in range(0, len(content)):
            while ('<TITLESTMT>' not in content[x]): 
                x=x+1
            title= re.findall(':.*?</TITLE>',content[x])[0][1:-8]
            break
        title=re.sub('\[','', title)
        title=re.sub('\]','', title)
        
        for x in range(0, len(content)):
            while ('<PERSNAME>' not in content[x]): 
                x=x+1
                if x  == len(content): 
                    break
            if x<len(content):
                author= re.findall('<PERSNAME>.*?</PERSNAME>',content[x])[0][10:-11]
            else: author= 'X'
            break
        author=re.sub('\[','', author)
        author=re.sub('\]','', author)
        if author=='unknown':
            author='X'
        
        for x in range(0, len(content)):
            while ('<PUBPLACE>' not in content[x]): 
                x=x+1
                if x  == len(content): 
                    break
            if x<len(content):
                pubplace = re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
            else: pubplace= 'X'
            break
        
        for x in range(0, len(content)):
            while ('<BOOKSELLER>' not in content[x]): 
                x=x+1
                if x  == len(content): 
                    break
            if x<len(content):
                bookseller= re.findall('<BOOKSELLER>.*?</BOOKSELLER>',content[x])[0][12:-13]
            else: bookseller= 'X'
            break
        
        for x in range(0, len(content)):
            while ('<IDNO TYPE="Wing">' not in content[x]): 
                x=x+1
                if x  == len(content): 
                    break
            if x<len(content):
                idno_wing= re.findall('<IDNO TYPE="Wing">.*?</IDNO>',content[x])[0][18:-7]
            else: idno_wing= 'X'
            break
        
        for x in range(0, len(content)):
            while ('<IDNO TYPE="Lamp">' not in content[x]): 
                x=x+1
                if x  == len(content): 
                    break
            if x<len(content):
                idno_lamp= re.findall('<IDNO TYPE="Lamp">.*?</IDNO>',content[x])[0][18:-7]
            else: idno_lamp= 'X'
            break
        
        
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
        
        written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=lampeter_corpus> <title=%s> <author=%s> <authorage=X> \
<pubdate=%s> <genre=tract, %s> <genre1=tract, %s> <place_of_publication=%s> <publisher=%s> <encoding=utf-8> \
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
    
def markup():
    extracted_path = r'H:\circle\text_extractor\new corpus\Lampeter\The Lampeter Corpus of Early Modern Tracts original\2400\extracted'
    cleaned_path = r'H:\circle\text_extractor\new corpus\Lampeter\The Lampeter Corpus of Early Modern Tracts original\2400\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'lawb1715.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file) as f:
            content = f.readlines()
        '''
        while x<len(content):
            open_count = content[x].count('<') 
            close_count = content[x].count('>') 
            if open_count > close_count:
                content[x] = content[x]+'>'
                content[x+1] = '<'+content[x+1]
            x=x+1
        ''' 
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        add_flag=0
        corr_flag=0
        bracket_flag = 0
        while x< len(content):
        
            if bracket_flag==1:
                content[x] = '<'+content[x]
                bracket_flag = 0
            
            open_count = content[x].count('<') 
            close_count = content[x].count('>') 
            if open_count > close_count:
                content[x] = content[x][:-1]
                content[x] = content[x]+'>'
                bracket_flag = 1

            if x>=1 and x<len(content)-1:
                
                if add_flag==1:
                    content[x]= '<ADD '+ content[x]
                    add_flag=0
                if content[x].endswith('<ADD\n'):
                    content[x]= content[x][:-5]
                    add_flag = 1
                    
                if corr_flag==1:
                    content[x]= '<CORR '+ content[x]
                    corr_flag=0
                if content[x].endswith('<CORR\n'):
                    content[x]= content[x][:-6]
                    corr_flag = 1
                    

                
                
                if 'ADD' in content[x]:
                    removes= re.findall('<ADD.*?/ADD>', content[x])
                    for remove in removes:
                        content[x] = re.sub(re.escape(remove), '', content[x])
                        
                if 'CORR' in content[x]:
                    removes= re.findall('<CORR.*?/CORR>', content[x])
                    for remove in removes:
                        #print(remove)
                        if 'SIC' in remove:
                            sub = re.findall('SIC=".*?"', remove)[0][5:-1]
                            content[x] = re.sub(re.escape(remove), sub, content[x])
                        else:
                            content[x]= re.sub(re.escape(remove), '', content[x])
                        
                     
                if '<' in content[x]:
                    #print(content[x])
                    removes= re.findall('<.*?>', content[x])
                    for remove in removes:
                        content[x] = re.sub(re.escape(remove), '', content[x])  


                #content[x] = re.sub(re.escape('N="(*)" PLACE="foot">'), '', content[x])
                '''
                if 'N=' in content[x]:
                    #print(content[x])
                    removes= re.findall('N=.*?>', content[x])
                    for remove in removes:
                        #print(remove)
                        content[x] = re.sub(remove, '', content[x])  
                        #print(content[x])
                
                        
                content[x] = re.sub('<Q', '', content[x])
                content[x] = re.sub('<PB', '', content[x])
                content[x] = re.sub('<FOREIGN', '', content[x])
                content[x] = re.sub('<FW', '', content[x])
                content[x] = re.sub('<CLOSER', '', content[x])
                content[x] = re.sub('<NOTE', '', content[x])
                content[x] = re.sub('<DEL', '', content[x])
                content[x] = re.sub('<SIGNED', '', content[x])
                content[x] = re.sub('<LIST', '', content[x])
                content[x] = re.sub('<LABEL', '', content[x])
                content[x] = re.sub('<PTR', '', content[x])
                content[x] = re.sub('<LG', '', content[x])
                content[x] = re.sub('<GAP', '', content[x])
                content[x] = re.sub('<BIBL', '', content[x])
                content[x] = re.sub('<CELL', '', content[x])
                content[x] = re.sub('<TRAILER', '', content[x])
                content[x] = re.sub('<ROW', '', content[x])
                content[x] = re.sub('<P', '', content[x])
                content[x] = re.sub('<HEAD', '', content[x])
                content[x] = re.sub('<L', '', content[x])
                content[x] = re.sub('<SPEAKER', '', content[x])
                '''

            if 1==1:
                content[x] = re.sub('&rehy;', '', content[x])
                content[x] = re.sub('&cross;', '', content[x])
                content[x] = re.sub('&dagger;', '', content[x])
                content[x] = re.sub('&dcross;', '', content[x])
                content[x] = re.sub('&descnode;', '', content[x])
                content[x] = re.sub('&dram;', '', content[x])
                content[x] = re.sub('&lphand;', '', content[x])
                content[x] = re.sub('&middot;', '', content[x])
                content[x] = re.sub('&min;', '', content[x])
                content[x] = re.sub('&ounce;', '', content[x])
                content[x] = re.sub('&para;', '', content[x])
                content[x] = re.sub('&rangle;', '', content[x])
                content[x] = re.sub('&rphand;', '', content[x])
                content[x] = re.sub('&scruple;', '', content[x])
                content[x] = re.sub('&sec;', '', content[x])
                content[x] = re.sub('&sect;', '', content[x])
                content[x] = re.sub('&verbar;', '', content[x])
                content[x] = re.sub('&ascnode;', '', content[x])
                content[x] = re.sub('&because;', '', content[x])
                content[x] = re.sub('&dag;', '', content[x])
                content[x] = re.sub('&dcross;', '', content[x])
                content[x] = re.sub('&deg;', '', content[x])
                
                content[x] = re.sub('&amp;', '&', content[x])
                content[x] = re.sub('&apos;', '’', content[x])
                content[x] = re.sub('&because;', '...', content[x])
                content[x] = re.sub('&therefore;', '...', content[x])
                content[x] = re.sub('&horbar;', '–', content[x])
                content[x] = re.sub('&horfill;', '–', content[x])
                content[x] = re.sub('&mdash;', '–', content[x])

                content[x] = re.sub('&Agrave;', 'À', content[x])
                content[x] = re.sub('&Aacute;', 'Á', content[x])
                content[x] = re.sub('&Acirc;', 'Â', content[x])
                content[x] = re.sub('&Atilde;', 'Ā', content[x])
                content[x] = re.sub('&Aring;', 'Â', content[x])
                content[x] = re.sub('&AElig;', 'AE', content[x])
                content[x] = re.sub('&Egrave;', 'È', content[x])
                content[x] = re.sub('&Eacute;', 'É', content[x])
                content[x] = re.sub('&Ecirc;', 'Ê', content[x])
                content[x] = re.sub('&Igrave;', 'Ì', content[x])
                content[x] = re.sub('&Iacute;', 'Í', content[x])
                content[x] = re.sub('&Icirc;', 'Î', content[x])
                content[x] = re.sub('&ETH;', 'Ð', content[x])
                content[x] = re.sub('&Ograve;', 'Ò', content[x])
                content[x] = re.sub('&Oacute;', 'Ó', content[x])
                content[x] = re.sub('&Ocirc;', 'Ô', content[x])
                content[x] = re.sub('&Otilde;', 'Ō', content[x])
                content[x] = re.sub('&Ugrave;', 'Ù', content[x])
                content[x] = re.sub('&Uacute;', 'Ú', content[x])
                content[x] = re.sub('&Ucirc;', 'Û', content[x])
                content[x] = re.sub('&THORN;', 'Þ', content[x])
                
                content[x] = re.sub('&agrave;', 'à', content[x])
                content[x] = re.sub('&aacute;', 'á', content[x])
                content[x] = re.sub('&acirc;', 'â', content[x])
                content[x] = re.sub('&atilde;', 'ā', content[x])
                content[x] = re.sub('&Aelig;', 'ae', content[x])
                content[x] = re.sub('&egrave;', 'è', content[x])
                content[x] = re.sub('&eacute;', 'é', content[x])
                content[x] = re.sub('&ecirc;', 'ê', content[x])
                content[x] = re.sub('&igrave;', 'ì', content[x])
                content[x] = re.sub('&iacute;', 'í', content[x])
                content[x] = re.sub('&icirc;', 'î', content[x])
                content[x] = re.sub('&eth;', 'ð', content[x])
                content[x] = re.sub('&ograve;', 'ò', content[x])
                content[x] = re.sub('&oacute;', 'ó', content[x])
                content[x] = re.sub('&ocirc;', 'ô', content[x])
                content[x] = re.sub('&otilde;', 'ō', content[x])
                content[x] = re.sub('&ugrave;', 'ù', content[x])
                content[x] = re.sub('&uacute;', 'ú', content[x])
                content[x] = re.sub('&ucirc;', 'û', content[x])
                content[x] = re.sub('&thorn;', 'þ', content[x])
                content[x] = re.sub('&OElig;', 'OE', content[x])
                content[x] = re.sub('&oelig;', 'oe', content[x])
                content[x] = re.sub('&mdash;', '–', content[x])
                content[x] = re.sub('&ndash;', '–', content[x])
                content[x] = re.sub('&rsquo;', '’', content[x])
                content[x] = re.sub('&prime;', '′', content[x])

                content[x] = re.sub('&rsup;', '=r=', content[x])
                content[x] = re.sub('&rsub;', 'r', content[x])
                content[x] = re.sub('&wynn;', 'ƿ', content[x])
                
                '''

                content[x] = re.sub('<q rend=it', '', content[x])
                content[x] = re.sub('<q rend=it', '', content[x])
                if x>2 and x< len(content)-1:
                    content[x] = re.sub('>', '', content[x])
                
                content[x] = re.sub('LANG="LAT"', '', content[x])
                content[x] = re.sub('LANG="FRA"', '', content[x])
                content[x] = re.sub('LANG="lat"', '', content[x])
                content[x] = re.sub('REND="it"', '', content[x])
                content[x] = re.sub('PLACE="margin"', '', content[x])
                content[x] = re.sub('TYPE="structure"', '', content[x])
                content[x] = re.sub('TYPE="catch"', '', content[x])
                content[x] = re.sub('TYPE="marginalia"', '', content[x])
                '''
                content[x] = re.sub('&', '', content[x])
                content[x] = re.sub('ic;', '', content[x])
                

            
                
                if x>1 and x!= len(content)-1 and 'ANCHORED="NO"' in content[x]:# and 'CORR' not in content[x]:
                    print('CHECK')
                    print(file)
                    print(content[x-1])
                    print(content[x])
                    #pass
                
                
                f.write(content[x])
                x=x+1

#extract()
markup()