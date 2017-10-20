# coding=utf-8

import os 
import re
import time
from collections import defaultdict

def filter_text(org):
    result= org
    return result


def initial():
    path_to_xml=r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\HC_XML_Master_v2.xml'
    
    
    with open(path_to_xml, encoding='utf-8') as f:
        content = f.readlines()
        
    
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
    


def mid_extracted():
    path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'
    file_number=0
    
    extracted_tei = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei\428.txt'
    extracted_tei_dir = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_tei'
    
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
            while ('<idno' not in content[x]): 
                x=x+1
                if x==len(content):
                    idno='FALSE'
                    break
        
            idno= re.findall('">.*?</idno>',content[x])[0][2:-7]
            break
        
        a_flag=0

        for x in range(0, len(content)):
            while ('<title level="m"' not in content[x]): 
                x=x+1
                if x==len(content):
                    for y in range(0, len(content)):
                        while ('<title level="a"' not in content[y]): 
                            y=y+1
                        title= re.findall('>.*?</title>',content[y])[0][1:-8]
                        a_flag=1
                        break
                    break
                        
            if a_flag==0:
                title= re.findall('<title level="m".*?</title>',content[x])[0][17:-1]
                break
        
        for x in range(0, len(content)):
            while ('<author key' not in content[x]): 
                x=x+1
        
            author= re.findall('key=".*?"',content[x])[0][5:-1]
            break
        if author=='X':
            author= 'Anonymous'
        
        for x in range(0, len(content)):
            while ('author_age' not in content[x]): 
                x=x+1
        
            authorage= re.findall('target=".*?"',content[x])[0][13:-1]
            break
        
        for x in range(0, len(content)):
            while ('<date type="manuscript"' not in content[x]): 
                x=x+1
        
            manuscriptdate= re.findall('>.*?<',content[x])[0][1:-1]
            break
        
        for x in range(0, len(content)):
            while ('<date type="original"' not in content[x]): 
                x=x+1
        
            originaldate= re.findall('>.*?<',content[x])[0][1:-1]
            break
            
    
        for x in range(0, len(content)):
            while ('<catRef n="T"' not in content[x]): 
                x=x+1
        
            genre1= re.findall('target="#.*?"',content[x])[0][9:-1]
            break
        
        '''
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
        title_date = title_date.replace('to ', '-')
        title_date = title_date.replace('–', '-')
        title_date = re.sub("[^1234567890-]", '', title_date)
        '''
            
        
        x=0
        while ('<text' not in content[x]): 
                x=x+1        
         
        while(x<len(content)-2):
            file_number = file_number+1
            file= os.path.join(path, str(file_number)+'.txt')
            f= open(file, 'w+', encoding='utf-8')
            
        
            written_header = '%s\n<file> <no=%s> <corpusnumber=%s> <corpus=helsinki_corpus_xml_edition> <title=%s> <author=%s> \
<dialect=Early Modern English> <authorage=%s> <manusript pubdate=%s> <original pubdate=%s> <genre1=%s> <genre2=X>  <encoding=utf-8> <text> \n\n' %(idno, file_number,corpus_number, title, author, authorage, manuscriptdate, originaldate, genre1)
        
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
            
    dict_prose= {}
    data_dict = defaultdict(list)
    final_dir = r'F:\freelance work\tepyML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_final_2'
            
    extracted_dir = r'F:\freelance work\tepyML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'
    files = os.listdir(extracted_dir)
    file_number=0
    prose_count=0
    for file in files:
        extracted= os.path.join(extracted_dir, file)
        print(extracted)
        
        with open(extracted, encoding='utf-8') as f:
            content = f.readlines()
            
            idno= content[0]
            header = content[1]
            footer= content[-1]
            
            div_exists= False
            for x in range(0, len(content)):
                if ('<div type="letter"' not in content[x]): 
                    pass
                else:
                    div_exists= True
            
            if div_exists:
                pass
                #a=1
                
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
                
                if idno in dict_prose:
                    f = open(dict_prose[idno], 'a', encoding='utf-8')
                    for x in range(2, len(content)):
                        f.write(content[x])
                    #f.write('\n\n')
                
                
                else:
                    file_number = file_number+1
                    file_new= os.path.join(final_dir, str(file_number)+'.txt')
                    
                    f= open(file_new, 'w+', encoding='utf-8')
                    for x in range(1, len(content)):
                        f.write(content[x])
                    #f.write('\n\n')
                    f.close
                    data_dict[idno].append(file_new)
                    dict_prose[idno]=file_new
                

    print(data_dict)


def porse_combine():
    porsedict= ( {'COPROGNO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\161.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\162.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\163.txt'], 'COMARVEL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\98.txt'], 'CEHIST2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3394.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3395.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3396.txt'], 'CEBOETH3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4622.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4623.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4624.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4625.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4626.txt'], 'CEDIAR3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4642.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4643.txt'], 'CETRAV3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4639.txt'], 'CESCIE1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2154.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2155.txt'], 'CEHAND3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4610.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4611.txt'], 'CMGAYTRY\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\830.txt'], 'COCHRIST\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\129.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\130.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\131.txt'], 'CELAW3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4605.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4606.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4607.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4608.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4609.txt'], 'CESERM1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2166.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2167.txt'], 'CMHORSES\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\273.txt'], 'COAELHOM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\81.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\82.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\83.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\84.txt'], 'CMCAXPRO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\841.txt'], 'CMKEMPE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\835.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\836.txt'], 'CODURHAM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\87.txt'], 'COQUADRU\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\68.txt'], 'CMAYENBI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\235.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\236.txt'], 'COCURA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\31.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\32.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\33.txt'], 'CESCIE2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3373.txt'], 'COAELET3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\88.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\89.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\90.txt'], 'COMARTYR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\107.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\108.txt'], 'COOHTWU3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\97.txt'], 'COLEOFRI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\176.txt'], 'CORUSHW\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\121.txt'], 'CMCTPROS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\326.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\327.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\328.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\329.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\330.txt'], 'CMVESHOM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\197.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\198.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\199.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\200.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\201.txt'], 'CEDIAR1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2186.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2187.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2188.txt'], 'CMPHLEBO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\274.txt'], 'CMMANKIN\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\855.txt'], 'CEDIAR2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3402.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3403.txt'], 'CMHANSYN\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\301.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\302.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\303.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\304.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\305.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\306.txt'], 'COCHROE4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\178.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\179.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\180.txt'], 'CORIDDLE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\151.txt'], 'COBENRUL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\85.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\86.txt'], 'CMGOWER\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\331.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\332.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\333.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\334.txt'], 'CESERM3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4627.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4628.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4629.txt'], 'CMVICES1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\221.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\222.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\223.txt'], 'CMCAPSER\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\828.txt'], 'CMSAWLES\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\212.txt'], 'CMROBGLO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\238.txt'], 'COLAW3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\45.txt'], 'CMLAW\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\793.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\794.txt'], 'COGENESI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\125.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\126.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\127.txt'], 'COAPOLLO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\109.txt'], 'COPHOENI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\153.txt'], 'CMDOCU4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\795.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\796.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\797.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\798.txt'], 'CEBIO3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4648.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4649.txt'], 'CMLAMBET\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\205.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\206.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\207.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\208.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\209.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\210.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\211.txt'], 'COLAW2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\11.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\12.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\13.txt'], 'CMALISAU\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\250.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\251.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\252.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\253.txt'], 'CMBEVIS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\248.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\249.txt'], 'COLACNU\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\66.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\67.txt'], 'CEHIST3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4637.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4638.txt'], 'CMWYCSER\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\284.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\285.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\286.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\287.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\288.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\289.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\290.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\291.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\292.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\293.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\294.txt'], 'CMHAVELO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\254.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\255.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\256.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\257.txt'], 'CMMIRK\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\829.txt'], 'CMEQUATO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\272.txt'], 'CODOCU4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\157.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\158.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\159.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\160.txt'], 'COEXETER\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\138.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\139.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\140.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\141.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\142.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\143.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\144.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\145.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\146.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\147.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\148.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\149.txt'], 'CMBESTIA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\237.txt'], 'CMNTEST\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\792.txt'], 'CMAELR3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\296.txt'], 'CEHAND2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3371.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3372.txt'], 'CETRI2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3389.txt'], 'CODREAM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\137.txt'], 'CMASTRO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\271.txt'], 'COBEDE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\36.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\37.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\38.txt'], 'CEBIO1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2190.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2191.txt'], 'CELAW1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2141.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2142.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2143.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2144.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2145.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2146.txt'], 'CMTRINIT\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\193.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\194.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\195.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\196.txt'], 'CODOCU1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\1.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\5.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\6.txt'], 'CESCIE2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3374.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3375.txt'], 'CMMARGA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\230.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\231.txt'], 'COGREGD4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\182.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\183.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\184.txt'], 'CEPLAY2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3413.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3414.txt'], 'CMFOXWO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\246.txt'], 'CESERM3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4630.txt'], 'CEFICT2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3412.txt'], 'COKENTIS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\132.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\133.txt'], 'CMBRUT3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\315.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\316.txt'], 'CEBOETH1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2161.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2162.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2163.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2164.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2165.txt'], 'CEHIST2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3392.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3393.txt'], 'COWSGOSP\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\119.txt'], 'CEFICT3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4650.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4651.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4652.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4653.txt'], 'CEHAND1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2149.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2150.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2151.txt'], 'CEEDUC1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2156.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2157.txt'], 'CEOTEST2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4598.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4599.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4600.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4601.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4602.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4603.txt'], 'CEPLAY3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4656.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4657.txt'], 'CMTHORN\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\799.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\800.txt'], 'CMCAPCHR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\842.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\843.txt'], 'CEEDUC2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3376.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3377.txt'], 'COAEPREF\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\91.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\92.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\93.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\94.txt'], 'CMAELR4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\833.txt'], 'CEOTEST1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3355.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3356.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3357.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3358.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3359.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3360.txt'], 'CMOTEST\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\786.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\787.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\788.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\789.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\790.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\791.txt'], 'CMMOON\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\243.txt'], 'CMSIRITH\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\244.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\245.txt'], 'CESERM1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2168.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2169.txt'], 'CEHAND3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4612.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4613.txt'], 'CMROLLBE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\839.txt'], 'CEFICT1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2202.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2203.txt'], 'CMMETHAM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\823.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\824.txt'], 'CMNORHOM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\280.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\281.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\282.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\283.txt'], 'COGREGD3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\104.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\105.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\106.txt'], 'CEPLAY3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4658.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4659.txt'], 'CMSIEGE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\852.txt'], 'CMCURSOR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\309.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\310.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\311.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\312.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\313.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\314.txt'], 'CMJULIA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\232.txt'], 'COPREFCP\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\34.txt'], 'COCHAD\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\181.txt'], 'CONORTHU\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\7.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\8.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\9.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\10.txt'], 'COOHTWU2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\39.txt'], 'COBRUNAN\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\44.txt'], 'CMCHAULI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\825.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\826.txt'], 'CMLUDUS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\853.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\854.txt'], 'COPARIPS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\118.txt'], 'COBLICK\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\76.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\77.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\78.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\79.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\80.txt'], 'CEDIAR2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3404.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3405.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3406.txt'], 'CEPLAY1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2204.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2205.txt'], 'CEFICT3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4654.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4655.txt'], 'CMTHRUSH\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\247.txt'], 'CMSELEG\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\242.txt'], 'CMDOCU3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\265.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\266.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\267.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\268.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\269.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\270.txt'], 'COBOETH\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\26.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\27.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\28.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\29.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\30.txt'], 'CMPOEMS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\262.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\263.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\264.txt'], 'CEHIST3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4635.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4636.txt'], 'CMPOEMH\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\239.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\240.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\241.txt'], 'CMPETERB\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\224.txt'], 'COLINDIS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\120.txt'], 'COCHROA3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\96.txt'], 'CMBRUT1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\225.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\226.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\227.txt'], 'COANDREA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\134.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\135.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\136.txt'], 'CEEDUC2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3378.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3379.txt'], 'CEFICT2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3410.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3411.txt'], 'CMROLLPS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2135.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2136.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2137.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2138.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2139.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2140.txt'], 'COMETRPS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\152.txt'], 'CETRAV3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4640.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4641.txt'], 'COOTEST\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\110.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\111.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\112.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\113.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\114.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\115.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\116.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\117.txt'], 'CMKATHE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\228.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\229.txt'], 'COBEOWUL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\150.txt'], 'CMHORN\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\258.txt'], 'CEBOETH2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3380.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3381.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3382.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3383.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3384.txt'], 'COEXODUS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\128.txt'], 'CEAUTO2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3407.txt'], 'COMETBOE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\154.txt'], 'CMFITZJA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\832.txt'], 'CMROYAL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\827.txt'], 'CMHILTON\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\838.txt'], 'COADRIAN\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\174.txt'], 'CMPERIDI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\186.txt'], 'CENTEST1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3361.txt'], 'COOROSIU\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\40.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\41.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\42.txt'], 'CEEDUC3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4619.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4620.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4621.txt'], 'CEDIAR1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2183.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2184.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2185.txt'], 'COWULF4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\165.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\166.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\167.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\168.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\169.txt'], 'CETRI3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4633.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4634.txt'], 'CMHALI\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\220.txt'], 'CMROLLTR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\840.txt'], 'CEBIO2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3408.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3409.txt'], 'COTEMPO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\71.txt'], 'CODICTS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\164.txt'], 'CESCIE3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4617.txt'], 'CODOCU3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\46.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\47.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\48.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\49.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\50.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\51.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\52.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\53.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\54.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\55.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\56.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\57.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\58.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\59.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\60.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\61.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\62.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\63.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\64.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\65.txt'], 'COCHROA2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\35.txt'], 'CETRI1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2170.txt'], 'CMPRICK\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\307.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\308.txt'], 'CESCIE3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4614.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4615.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4616.txt'], 'COEPIHOM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\170.txt'], 'CEHIST1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2176.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2177.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2178.txt'], 'CMPURVEY\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\297.txt'], 'CMCLOUD\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\298.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\299.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\300.txt'], 'CMEDMUND\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\846.txt'], 'CMANCRE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\214.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\215.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\216.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\217.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\218.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\219.txt'], 'COINSPOL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\171.txt'], 'CEDIAR3B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4644.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4645.txt'], 'CETRAV2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3397.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3398.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3399.txt'], 'CEHAND2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3369.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3370.txt'], 'COSOLOMO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\175.txt'], 'CMINNOCE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\831.txt'], 'CEAUTO1\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2189.txt'], 'CMJULNOR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\837.txt'], 'CEHIST1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2171.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2172.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2173.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2174.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2175.txt'], 'CMCTVERS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\322.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\323.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\324.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\325.txt'], 'COPREFSO\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\177.txt'], 'CMROOD\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\213.txt'], 'CETRI2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3390.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3391.txt'], 'CETRI3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4631.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4632.txt'], 'CESERM2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3387.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3388.txt'], 'CEPLAY2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3415.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3416.txt'], 'COBYRHTF\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\69.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\70.txt'], 'CMVICES4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\834.txt'], 'COVESPS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\43.txt'], 'CEFICT1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2192.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2193.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2194.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2195.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2196.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2197.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2198.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2199.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2200.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2201.txt'], 'CMBOETH\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\275.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\276.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\277.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\278.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\279.txt'], 'CELAW2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3362.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3363.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3364.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3365.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3366.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3367.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3368.txt'], 'CETRAV1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2179.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2180.txt'], 'CMTOWNEL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\856.txt'], 'CMEARLPS\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\259.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\260.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\261.txt'], 'COLAW4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\155.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\156.txt'], 'CENTEST2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4604.txt'], 'COAELIVE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\100.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\101.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\102.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\103.txt'], 'CESCIE1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2152.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2153.txt'], 'CMBENRUL\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\295.txt'], 'CETRAV1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2181.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2182.txt'], 'CMKENTSE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\234.txt'], 'CEAUTO3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4646.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4647.txt'], 'COWULF3\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\72.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\73.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\74.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\75.txt'], 'CODOCU2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\14.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\15.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\16.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\17.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\18.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\19.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\20.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\21.txt'], 'CESERM2A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3385.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3386.txt'], 'CMDOCU2\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\233.txt'], 'CEEDUC1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2158.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2159.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2160.txt'], 'COLAECE\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\22.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\23.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\24.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\25.txt'], 'CEPLAY1B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2206.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2207.txt'], 'COALEX\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\99.txt'], 'CMGREGOR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\844.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\845.txt'], 'COAEPREG\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\95.txt'], 'CEEDUC3A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\4618.txt'], 'CMYORK\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\857.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\858.txt'], 'COCYNEW\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\122.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\123.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\124.txt'], 'CMMANDEV\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\320.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\321.txt'], 'CMBODLEY\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\202.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\203.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\204.txt'], 'COAELET4\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\172.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\173.txt'], 'CMREYNES\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\801.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\802.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\803.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\804.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\805.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\806.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\807.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\808.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\809.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\810.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\811.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\812.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\813.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\814.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\815.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\816.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\817.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\818.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\819.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\820.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\821.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\822.txt'], 'COMARGA\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\185.txt'], 'CMORM\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\187.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\188.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\189.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\190.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\191.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\192.txt'], 'CMPOLYCH\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\317.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\318.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\319.txt'], 'CETRAV2B\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3400.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\3401.txt'], 'CMMALORY\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\849.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\850.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\851.txt'], 'CMREYNAR\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\847.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\848.txt'], 'CEHAND1A\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2147.txt', 'H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\2148.txt'], 'CMDIGBY\n': ['H:\\circle\\tepyXML Helsinki Corpus Browser\\XML Helsinki Corpus Browser\\hcbrow\\corpus\\extracted_final\\859.txt']})
    print(porsedict)
    
    for item in porsedict:
        print(item)
        files = porsedict[item]
        for file in files:
            pass
        
        
def clean_up():
    pass
    final_dir = r'F:\freelance work\tepyML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_final_2'
    cleaned_dir = r'F:\freelance work\tepyML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\cleaned'
    
    files = os.listdir(final_dir)
    for file in files:
        extracted= os.path.join(final_dir, file)
        
        with open(extracted, encoding='utf-8') as f:
            content = f.readlines()
            
        cleaned = os.path.join(cleaned_dir, file)
        c = open(cleaned, 'w+', encoding='utf-8')
        for x in range(0, len(content)):
            
            line = content[x]
            if x>5:
                if x<len(content)-5:
                    line = re.sub('</text> </file>', '', line) 
            
            
            line = re.sub('<sic resp.+</sic>', '', line)
            
            line = re.sub('<supplied resp.+</supplied>', '', line)
            line = re.sub('<note resp="#xpath1.+</note>', '', line)
            line = re.sub('<note resp="#HC_.+</note>', '', line)
            line = re.sub('<note.+/note>', '', line)
            line = re.sub('&amp;', '&', line)
            line = re.sub('&amp', '&', line)
            line = re.sub('<am/>', '~', line)
            line = re.sub('<cb.+</cb>', '', line)
            
            line = re.sub('<hi rend="sup">', '', line)
            line = re.sub('</hi>', '~', line)
            
            
            line = re.sub('<lb/>', '', line)
            line = re.sub('<p>', '', line)
            line = re.sub('</p>', '', line)
            line = re.sub('<am/>', '', line)
            line = re.sub('<pb.+/>', '', line)
            line = re.sub('<foreign>', '', line)
            line = re.sub('</foreign>', '', line)
            line = re.sub('<milestone.+/>', '', line)
            
            line = re.sub('<div.+>', '', line)
            line = re.sub('</div>', '', line)
            line = re.sub('<head.+/head>', '', line)
            line = re.sub('<head>', '', line)
            line = re.sub('</head>', '', line)
            line = re.sub('<opener>', '', line)
            line = re.sub('</opener>', '', line)
            
            line = re.sub('<lg>', '', line)
            line = re.sub('</lg>', '', line)
            line = re.sub('<l>', '', line)
            line = re.sub('</l>', '', line)  
            
            line = re.sub('<note type="address">', '', line)
            line = re.sub('</note>', '', line)  
            
            line = re.sub('<choice>', '', line)  
            line = re.sub('</choice>', '', line)  
            line = re.sub('<corr resp="#HC_XML_errata_corrections">', '', line) 
            line = re.sub('</corr>', '', line) 
            line = re.sub('<sp>', '', line) 
            line = re.sub('</sp>', '', line) 
            
            line = re.sub('<hi rend="type">', '', line) 
            line = re.sub('<hi rend="sup">', '', line) 
            line = re.sub('</hi>', '', line) 
            
            line = re.sub('<supplied>', '', line) 
            line = re.sub('</supplied>', '', line) 
            line = re.sub('<closer>', '', line) 
            line = re.sub('</closer>', '', line) 
            line = re.sub('<note>', '', line) 
            line = re.sub('</note>', '', line)  
            
            
            c.write(line)
            
        c.close()
            
        


def markup():
    extracted_path = r'H:\circle\tepyML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_final_2'
    cleaned_path = r'H:\circle\tepyML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file) as f:
            print(path_extracted_file)
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        while x< len(content):
            
            if '<comment' in content[x]:
                while '/comment>' not in content[x]:
                    x=x+1
                x=x+1
 
            else:
                if x>1:
                    content[x] = re.sub('_', '', content[x])
                else:
                    content[x] = re.sub('unknown', 'X', content[x])
                    content[x] = re.sub('</title', '', content[x])
                    content[x] = re.sub('<dialect=Early Modern English> ', '', content[x])
                
                    content[x] = re.sub('manusript', 'manuscript', content[x])
                    content[x] = re.sub('<genre2=X> ', '', content[x])
                    content[x] = re.sub('under', '-', content[x])
                    content[x] = re.sub('over', '+', content[x])
                    content[x] = re.sub('anonymous', 'X', content[x])
                    content[x] = re.sub('genre1', 'genre', content[x])
                    content[x] = re.sub('let.priv', 'letter', content[x])
                    content[x] = re.sub('let.non-priv', 'letter', content[x])

            if x>5:
                if x<len(content)-5:
                    content[x] = re.sub('</text> </file>', '', content[x]) 
            
            
            content[x] = re.sub('<sic resp.+</sic>', '', content[x])
            
            content[x] = re.sub('<supplied resp.+</supplied>', '', content[x])
            #content[x] = re.sub('<note resp="#xpath1.+</note>', '', content[x])
            #content[x] = re.sub('<note resp="#HC_.+</note>', '', content[x])
            #content[x] = re.sub('<note.+/note>', '', content[x])
            content[x] = re.sub('&amp;', '&', content[x])
            content[x] = re.sub('&amp', '&', content[x])
            content[x] = re.sub('<am/>', '~', content[x])
            content[x] = re.sub('<cb.+</cb>', '', content[x])
            
            content[x] = re.sub('<hi rend="sup">', '', content[x])
            content[x] = re.sub('</hi>', '~', content[x])
            
            
            content[x] = re.sub('<lb/>', '', content[x])
            content[x] = re.sub('<p>', '', content[x])
            content[x] = re.sub('</p>', '', content[x])
            content[x] = re.sub('<am/>', '', content[x])
            content[x] = re.sub('<pb.+/>', '', content[x])
            content[x] = re.sub('<foreign>', '', content[x])
            content[x] = re.sub('</foreign>', '', content[x])
            content[x] = re.sub('<milestone.+/>', '', content[x])
            
            content[x] = re.sub('<div.+>', '', content[x])
            content[x] = re.sub('</div>', '', content[x])
            content[x] = re.sub('<head.+/head>', '', content[x])
            content[x] = re.sub('<head>', '', content[x])
            content[x] = re.sub('</head>', '', content[x])
            content[x] = re.sub('<opener>', '', content[x])
            content[x] = re.sub('</opener>', '', content[x])
            
            content[x] = re.sub('<lg>', '', content[x])
            content[x] = re.sub('</lg>', '', content[x])
            content[x] = re.sub('<l>', '', content[x])
            content[x] = re.sub('</l>', '', content[x])  
            
            #content[x] = re.sub('<note type="address">', '', content[x])
            #content[x] = re.sub('</note>', '', content[x])  
            
            content[x] = re.sub('<choice>', '', content[x])  
            content[x] = re.sub('</choice>', '', content[x])  
            content[x] = re.sub('<corr resp="#HC_XML_errata_corrections">', '', content[x]) 
            content[x] = re.sub('</corr>', '', content[x]) 
            content[x] = re.sub('<sp>', '', content[x]) 
            content[x] = re.sub('</sp>', '', content[x]) 
            
            content[x] = re.sub('<hi rend="type">', '', content[x]) 
            content[x] = re.sub('<hi rend="sup">', '', content[x]) 
            content[x] = re.sub('</hi>', '', content[x]) 
            
            content[x] = re.sub('<supplied>', '', content[x]) 
            content[x] = re.sub('</supplied>', '', content[x]) 
            content[x] = re.sub('<closer>', '', content[x]) 
            content[x] = re.sub('</closer>', '', content[x]) 
            #content[x] = re.sub('<note>', '', content[x]) 
            #content[x] = re.sub('</note>', '', content[x])  
                
                
            if x>1 and x!= len(content)-1 and '<' in content[x]:
                print(content[x])
                break
            
            f.write(content[x])
            x=x+1
            
            

#initial()
print('Start')
#mid_extracted()
#final_extracted()   
#clean_up()
markup()