# coding=utf-8

import os 
import re
import time

def filter_text(org):
    result= org
    return result


def initial():
    path_to_xml=r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\HC_XML_Master_v2.xml'
    
    
    with open(path_to_xml, encoding='utf-8') as f:
        content = f.readlines()
        
    
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
    


def mid_extracted():
    path = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'
    file_number=0
    
    extracted_tei = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei\428.txt'
    extracted_tei_dir = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei'
    
    files = os.listdir(extracted_tei_dir)
    for file in files:
        extracted_tei2= os.path.join(extracted_tei_dir, file)
        
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
            
    
        for x in range(0, len(content)):
            while ('<catRef n="T"' not in content[x]): 
                x=x+1
        
            genre1= re.findall('target="#.*?"',content[x])[0][9:-1]
            break
        
        
        title_date=pubdate
        for x in range(0, len(content)):
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
        title_date = title_date.replace('to ', '-')
        title_date = title_date.replace('–', '-')
        title_date = re.sub("[^1234567890-]", '', title_date)
        print(title_date)
            
        
        x=0
        while ('<text' not in content[x]): 
                x=x+1        
         
        while(x<len(content)-2):
            file_number = file_number+1
            file= os.path.join(path, str(file_number)+'.txt')
            f= open(file, 'w+', encoding='utf-8')
            
        
            written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=helsinki_corpus_xml_edition> <title=%s> <author=%s> \
<dialect=Early Modern English> <authorage=%s> <pubdate=%s> <genre1=%s> <genre2=X>  <encoding=utf-8> <text> \n\n' %(file_number,corpus_number, title, author, authorage, title_date, genre1)
        
            f.write(written_header)
            
    
        
            while ('<div type="sample"' not in content[x]): 
                x=x+1
                if x== len(content)-1:
                    break
            if x== len(content)-1:
                f.close()
                os.remove(file)
                file_number = file_number-1
                break
            div_count=-1
            while ('</div>' not in content[x] or   div_count>0): 
                if '<div' in content[x]:
                    div_count=div_count+1
    
                if '</div' in content[x]:
                    div_count=div_count-1
    
                    
                res= filter_text(content[x])
                f.write(res[6:])
                x=x+1
            res= filter_text(content[x])
            f.write(res[6:])
            f.write('\n</text> </file>')
            x=x+1
        
        f.close()


        

        
        
def final_extracted():  
            
    
    final_dir = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_final'
            
    extracted_dir = r'H:\circle\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'
    files = os.listdir(extracted_dir)
    file_number=0
    for file in files:
        extracted= os.path.join(extracted_dir, file)
        print(extracted)
        
        with open(extracted, encoding='utf-8') as f:
            content = f.readlines()
            
            header = content[0]
            footer= content[-1]
            
            div_exists= False
            for x in range(0, len(content)):
                if ('<div type="letter"' not in content[x]): 
                    pass
                else:
                    div_exists= True
            
            if div_exists:
                for x in range(0, len(content)):
                    
                    while ('<div type="letter"' not in content[x]):   
                        x=x+1 
                        if x==len(content):
                            break
                    
                    if x<len(content):
                        file_number = file_number+1
                        file_new= os.path.join(final_dir, str(file_number)+'.txt')
                        f= open(file_new, 'w+', encoding='utf-8')
                        f.write(header)
                        f.write('\n')
        
                        while ('</div>' not in content[x]):
                            f.write(content[x])   
                            x=x+1  
                        f.write(content[x])
                        f.write('\n')
                        f.write(footer)
    
            else:
                file_number = file_number+1
                file_new= os.path.join(final_dir, str(file_number)+'.txt')
                f= open(file_new, 'w+', encoding='utf-8')
                for x in range(0, len(content)):
                    f.write(content[x])
                f.close
            
            
#initial()
#mid_extracted()
final_extracted()    