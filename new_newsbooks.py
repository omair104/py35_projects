import os,re,time
from ctypes.test.test_pep3118 import Complete

def extract():
    org_path = r'H:\circle\py\new corpus\Newsbooks\The Lancaster Newsbooks Corpus (17th century)\2531\all'
    extracted_path = r'H:\circle\py\new corpus\Newsbooks\The Lancaster Newsbooks Corpus (17th century)\2531\extracted'
    
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
            while ('<title>' not in content[x]): 
                x=x+1
            title= re.findall('<title>.*?</title>',content[x])[0][7:-8]
            break
        
        if filename.startswith('MFum'):
            pubdate='1654-1655'
        else:
            pubdate='1653-1654'
        
        
        written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=lancaster_newsbooks_corpus> <title=%s> \
<pubdate=%s> <genre=newsbook> <encoding=utf-8> <text> \n' %(file_number,filename, title, pubdate)
        
        print(written_header)
        
        
        file= os.path.join(extracted_path, str(filename)+'.txt')
        f= open(file, 'w+', encoding='utf-8')
        f.write(written_header)
        
        x=0
        while ('<p>' not in content[x]): 
            x=x+1         
         
        while(x<len(content)-1):        
            f.write(content[x])
            x=x+1
        f.write('\n</text> </file>')
        f.close
        
def markup():
    extracted_path = r'H:\circle\py\new corpus\Newsbooks\The Lancaster Newsbooks Corpus (17th century)\2531\extracted'
    cleaned_path = r'H:\circle\py\new corpus\Newsbooks\The Lancaster Newsbooks Corpus (17th century)\2531\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #print(file)
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file) as f:
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        while x< len(content):
            
            if '<!' in content[x]:
                    #print(content[x])
                    removes= re.findall('<!.*?>', content[x])
                    for remove in removes:
                        #print(remove)
                        #print(content[x])
                        content[x] = re.sub(re.escape(remove), '', content[x])  
            
            if '<head' in content[x]:
                while '/head>' not in content[x]:
                    x=x+1
                x=x+1
                
            elif '<pb' in content[x]:
                x=x+1
                
            elif '<img' in content[x]:
                x=x+1
                
            elif '<poem' in content[x]:
                x=x+1
                
                
            else:
                if '<reg' in content[x]:
                    #org_word= re.findall('orig=".*?">',content[x])[0][6:-2]
                    org_words= re.findall('orig=".*?">',content[x])
                    completes= re.findall('<reg.*?/reg>',content[x])

                    for y in range(len(org_words)):
                        print(file)
                        print(content[x])
                        print(org_words)
                        print(y)
                        print(completes)
                        org_word= org_words[y][6:-2]
                        complete = completes[y]
                        #print(org_word)
                        #print(complete)
                        content[x] = re.sub(complete, org_word, content[x])
                        
                content[x] = re.sub('&amp;', '&', content[x])
                content[x] = re.sub('&apos;', '\'', content[x])
                content[x] = re.sub('&nbsp', ' ', content[x])
            
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
                
                content[x] = re.sub('&ldquo;', '', content[x])
                content[x] = re.sub('&rdquo;', '', content[x])
                content[x] = re.sub('&#x261e;', '', content[x])
                content[x] = re.sub('&#x2014;', '', content[x])
                content[x] = re.sub('&#x2648;', '', content[x])
                content[x] = re.sub('&#x2720;', '', content[x])
                content[x] = re.sub('&tilde;', '', content[x])
                
                content[x] = re.sub('<p>', '', content[x])
                content[x] = re.sub('</p>', '', content[x])
                content[x] = re.sub('<i>', '', content[x])
                content[x] = re.sub('</i>', '', content[x])
                content[x] = re.sub('<newsbookHeader>', '', content[x])
                content[x] = re.sub('</newsbookHeader>', '', content[x])
                content[x] = re.sub('<newsbookText>', '', content[x])
                content[x] = re.sub('</newsbookText>', '', content[x])
                content[x] = re.sub('<newsbookDoc>', '', content[x])
                content[x] = re.sub('</newsbookDoc>', '', content[x])
                content[x] = re.sub('<hr />', '', content[x])
                content[x] = re.sub('<em>', '', content[x])
                content[x] = re.sub('</em>', '', content[x])
                content[x] = re.sub('<unclear>', '', content[x])
                content[x] = re.sub('</unclear>', '', content[x])
                content[x] = re.sub('<line>', '', content[x])
                content[x] = re.sub('</line>', '', content[x])
                content[x] = re.sub('<stanza>', '', content[x])
                content[x] = re.sub('</stanza>', '', content[x])
                content[x] = re.sub('<poem>', '', content[x])
                content[x] = re.sub('</poem>', '', content[x])
                content[x] = re.sub('<go>', '', content[x])
                content[x] = re.sub('</go>', '', content[x])
                content[x] = re.sub('<tr>', '', content[x])
                content[x] = re.sub('</tr>', '', content[x])
                content[x] = re.sub('<table>', '', content[x])
                content[x] = re.sub('</table>', '', content[x])
                content[x] = re.sub('<reg>', '', content[x])
                content[x] = re.sub('</reg>', '', content[x])
                content[x] = re.sub('<td>', '', content[x])
                content[x] = re.sub('</td>', '', content[x])
                

                content[x] = re.sub('<note place="side" id="N01">', '', content[x])
                content[x] = re.sub('</note', '', content[x])
                content[x] = re.sub('<ptr target="N01"/>', '', content[x])
                content[x] = re.sub('<td colspan="3" rowspan="3">', '', content[x])
                
                if x>1 and x!= len(content)-1 and '<' in content[x]:
                    print(content[x])
                
    
                f.write(content[x])
                x=x+1


#extract()
markup()
    