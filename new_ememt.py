import os,re


def extract():
    org_path = r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT Full Corpus\EMEMT Full Corpus\EMEMT_Corpus\All'
    extracted_path = r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT Full Corpus\EMEMT Full Corpus\EMEMT_Corpus\extracted'
    
    files = os.listdir(org_path)
    #print(files)
    file_number=0
    for file in files:
        
        
        
        
        if os.path.splitext(file)[1]=='.html' and 'NORM' not in file and '_pt' not in file:
            print(file)
        
            file_number= file_number+1
            path_org_file= os.path.join(org_path, file)
            
            
            with open(path_org_file) as f:
                content = f.readlines()
                
            filename= file[:-10]
    
            
            for x in range(0, len(content)):
                while ('<p><strong>Year of publication:' not in content[x]): 
                    x=x+1
                pubdate= re.findall('</strong>.*?</p>',content[x])[0][10:14]
                break
            
            
            
            for x in range(0, len(content)):
                while ('<p><strong>Author:</strong>' not in content[x]): 
                    x=x+1
                author= re.findall('</strong>.*?\n',content[x])[0][10:-5]
                break
            
            print(author)
            
            for x in range(0, len(content)):
                while ('<p><strong>Dates of birth and death:</strong>' not in content[x]): 
                    x=x+1
                    if x  == len(content): 
                        break
                if x<len(content):
                    dob= re.findall('</strong>.*?\n',content[x])[0]
                else: dob=''
                #dob.replace('-', ' ')
                #dob2= [int(s) for s in dob.split() if s.isdigit()]
                dob2= re.findall(r'\d{4}', dob)
                if len(dob2)==2:
                    dob3= dob2[0]+'-'+dob2[-1]
                else: dob3=''
                break
            
            for x in range(0, len(content)):
                while ('<p><strong>Publishing information' not in content[x]): 
                    x=x+1
                pub_info= re.findall('</strong>.*?\n',content[x])[0][10:-5]
                a = pub_info.split(':')
                break
            if len(a)==2:
                place_publication= a[0]
                publisher = a[1]
            
            for x in range(0, len(content)):
                while ('<p><strong>Catalogue number:</strong>' not in content[x]): 
                    x=x+1
                idno= re.findall('</strong>.*?</p>',content[x])[0][10:-5][-5:]
                break
            
            written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=early_modern_english_medical_texts> <author=%s> \
<dialect=Early Modern English> <dates_of_birth_and_death=%s> <pubdate=%s> <place_of_publication=%s> <publisher=%s> <genre=medical> <idno=%s>  <encoding=utf-8> <text> \n' %(file_number,filename, author, dob3, pubdate, place_publication, publisher, idno)
            
            print(written_header)
        
            file= os.path.join(extracted_path, str(filename)+'.txt')
            f= open(file, 'w+', encoding='utf-8')
            f.write(written_header)
            
            path_org_file2= os.path.join(org_path, filename + '.txt')
            with open(path_org_file2) as g:
                content_text = g.readlines()
            x=0      
            while(x<len(content_text)-1):        
                f.write(content_text[x])
                x=x+1
            f.write('\n</text> </file>')
            f.close
        
        
        
def markup():
    extracted_path = r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT Full Corpus\EMEMT Full Corpus\EMEMT_Corpus\extracted'
    cleaned_path = r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT Full Corpus\EMEMT Full Corpus\EMEMT_Corpus\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file) as f:
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        while x< len(content):
            
            if '[^' in content[x]:
                while '^]' not in content[x]:
                    x=x+1
                x=x+1
                
            elif '[/' in content[x]:
                while '/]' not in content[x]:
                    x=x+1
                x=x+1
            
            else:
                content[x] = re.sub('&amp;', '&', content[x])
                content[x] = re.sub('&quot;', '', content[x])
                content[x] = re.sub('_', '', content[x])
                content[x] = re.sub('/', '', content[x])
                content[x] = re.sub('\[}', '', content[x])
                content[x] = re.sub('}\]', '', content[x])
                
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
                
        
                
                f.write(content[x])
                x=x+1
            
markup()