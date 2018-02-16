# -*- coding: utf-8 -*-
import os,re

def extract():
    org_path = r'C:\data\EEBO Phase 1\New folder2'
    extracted_path = r'C:\data\EEBO Phase 1\EEBO TCP Phase 1'
    #org_path = r'C:\data\EEBO_new\New folder2'
    #extracted_path = r'C:\data\EEBO_new\extracted'
    file_number=0
    g=open(r'C:\data\EEBO Phase 1\plus_words.txt', 'w')
    #files = os.listdir(org_path)
    for path, subdirs, files in os.walk(org_path):
        for filename in files:
            if os.path.splitext(filename)[1] == '.xml':
                file = os.path.join(path, filename)
                #print(file)
                
                #print(file_number)
                file_number= file_number+1
                path_org_file= file
                
                #print(path_org_file)
                
                with open(path_org_file, encoding='utf8') as f:
                    content = f.readlines()
                    
                filename= filename[:-11]
                #print(filename)
                
                for x in range(0, len(content)):
                    while ('<TITLESTMT><TITLE TYPE="' not in content[x]): 
                        x=x+1
                    title= re.findall('">.*?</TITLE>',content[x])[0][2:-8]
                    break
                #print(title)
                if title[-1]=='.':
                    title = title[:-1]
                
                for x in range(0, len(content)):
                    while ('<AUTHOR>' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        author= re.findall('<AUTHOR>.*?</AUTHOR>',content[x])[0][8:-10]
                    else: author='X'
                    break
                #print(author)
                if author == '':
                    author = 'X'
                
                for x in range(10, len(content)):
                    while ('<PUBPLACE>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            place_of_pub= ''
                            break
                    if x !=len(content)-1:
                        place_of_pub= re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
                        break
                    else:
                        break
                place_of_pub = re.sub("[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]", '', place_of_pub)
                    
                for x in range(10, len(content)):
                    while ('<PUBLISHER>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            publisher= ''
                            break
                    if x !=len(content)-1:
                        publisher= re.findall('<PUBLISHER>.*?</PUBLISHER>',content[x])[0][11:-12]
                        break
                    else:
                        break
                    
                for x in range(0, len(content)):
                    while ('<TERM>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            keywords= ''
                            break
                    if x !=len(content)-1:
                        keywords= re.findall('<TERM>.*?</TERM>',content[x])[0][6:-7]
                        break
                    else:
                        break

                
                
                if place_of_pub in ['ImprintedatLondon', 'PrintedatLondon', 'Londini', 'AtLondon', 'ImpryntedatLondon', 'EnpryntedatLondon', 'Londonprinted']:
                    place_of_pub = 'London'
                if place_of_pub in ['PrintedatOxfordieLondon', 'OxfordieLondon']:
                    place_of_pub= 'Oxford and London'
                if place_of_pub =='FrancofortiadMoenum':
                    place_of_pub= 'Frankfurt am Main'
                if place_of_pub =='ImprentitatEdinburgh':
                    place_of_pub= 'Edinburgh'
                
                for x in range(10, len(content)):
                    while ('<DATE>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            pubdate= ''
                            break
                    if x!= len(content)-1:
                        #print(content[x])
                        pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
                        break
                    else:
                        break
                #print(pubdate)
                pubdate = re.sub("[^0123456789]", '', pubdate)
                pubdate = pubdate[-4:]
                
                for x in range(0, len(content)):
                    while ('<IDNO TYPE="stc">' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        idno= re.findall('<IDNO TYPE="stc">.*?</IDNO>',content[x])[0][17:-7]
                        break
                    else: 
                        idno = 'X'
                        break
                #print(idno)
                
                
                
                written_header = '<file> <no=%s> <filename=%s> <corpus=early_english_books_online> <title=%s> <author=%s> \
<pubdate=%s> <keywords=%s> <place_of_publication=%s> <publisher=%s> <idno=%s> <encoding=utf-8> <text> \n' %(file_number,filename, title, author, pubdate, keywords, place_of_pub, publisher, idno)
                
                
                
                file= os.path.join(extracted_path, str(filename)+'.txt')
                f= open(file, 'w+', encoding='utf-8')
                f.write(written_header)
                
                x=0
                 
                while(x<len(content)-1):      
                    
                    if '+' in content[x]:
                        g.write(content[x])  
                        
                    f.write(content[x])
                    x=x+1
                f.write('\n</text> </file>')
                f.close
                
def subcorpus():
    org_path = r'C:\data\EEBO Phase 1\New folder2'
    extracted_path = r'C:\data\EEBO Phase 1\EEBO Phase 1 samples'
    file_number=0
    #files = os.listdir(org_path)
    all_dates= list(range(1500,1701))
    all_dates.extend(list(range(1500,1701)))
    #all_dates.extend(list(range(1500,1701)))
    #print(all_dates)

    for path, subdirs, files in os.walk(org_path):
        for filename in files:
            if os.path.splitext(filename)[1] == '.xml':
                file = os.path.join(path, filename)
                #print(file)
                
                #print(file_number)
                
                path_org_file= file
                
                #print(path_org_file)
                
                with open(path_org_file, encoding='utf8') as f:
                    content = f.readlines()
                    
                filename= filename[:-11]
                #print(filename)
                
                for x in range(0, len(content)):
                    while ('<TITLESTMT><TITLE TYPE="' not in content[x]): 
                        x=x+1
                    title= re.findall('">.*?</TITLE>',content[x])[0][2:-8]
                    break
                #print(title)
                if title[-1]=='.':
                    title = title[:-1]
                
                for x in range(0, len(content)):
                    while ('<AUTHOR>' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        author= re.findall('<AUTHOR>.*?</AUTHOR>',content[x])[0][8:-10]
                    else: author='X'
                    break
                #print(author)
                if author == '':
                    author = 'X'
                
                for x in range(10, len(content)):
                    while ('<PUBPLACE>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            place_of_pub= ''
                            break
                    if x !=len(content)-1:
                        place_of_pub= re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
                        break
                    else:
                        break
                #print(place_of_pub)
                place_of_pub = re.sub("[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]", '', place_of_pub)
                if place_of_pub in ['ImprintedatLondon', 'PrintedatLondon', 'Londini', 'AtLondon', 'ImpryntedatLondon', 'EnpryntedatLondon', 'Londonprinted']:
                    place_of_pub = 'London'
                if place_of_pub in ['PrintedatOxfordieLondon', 'OxfordieLondon']:
                    place_of_pub= 'Oxford and London'
                if place_of_pub =='FrancofortiadMoenum':
                    place_of_pub= 'Frankfurt am Main'
                if place_of_pub =='ImprentitatEdinburgh':
                    place_of_pub= 'Edinburgh'
                    
                for x in range(10, len(content)):
                    while ('<DATE>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            pubdate= ''
                            break
                    if x!= len(content)-1:
                        #print(content[x])
                        pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
                        break
                    else:
                        break
                #print(pubdate)
                pubdate = re.sub("[^0123456789]", '', pubdate)
                pubdate = pubdate[-4:]
                
                for x in range(0, len(content)):
                    while ('<IDNO TYPE="stc">' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        idno= re.findall('<IDNO TYPE="stc">.*?</IDNO>',content[x])[0][17:-7]
                        break
                    else: 
                        idno = 'X'
                        break
                #print(idno)
                
                for x in range(10, len(content)):
                    while ('<PUBLISHER>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            publisher= ''
                            break
                    if x !=len(content)-1:
                        publisher= re.findall('<PUBLISHER>.*?</PUBLISHER>',content[x])[0][11:-12]
                        break
                    else:
                        break
                    if publisher[-1] ==',':
                        publisher= publisher[:-1]
                    
                for x in range(0, len(content)):
                    while ('<TERM>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            keywords= ''
                            break
                    if x !=len(content)-1:
                        keywords= re.findall('<TERM>.*?</TERM>',content[x])[0][6:-7]
                        if keywords[-1] =='.':
                            keywords= keywords[:-1]
                        if keywords=='':
                            keywords='X'
                        break
                    else:
                        break
                
                
                
                               
                for n in all_dates:
                    if str(n) in pubdate:

                        file= os.path.join(extracted_path, str(n)+'_'+str(filename)+'.txt')
                        f= open(file, 'w+', encoding='utf-8')
                        file_number= file_number+1
                        
                        written_header = '<file> <no=%s> <filename=%s> <corpus=EEBO_samples> <title=%s> <author=%s> \
<pubdate=%s> <keywords=%s> <place_of_publication=%s> <publisher=%s> <idno=%s> <encoding=utf-8> <text> \n' %(file_number,filename, title, author, pubdate, keywords, place_of_pub, publisher, idno)

                        f.write(written_header)
                        
                        x=0
                        while ('<TEXT>' not in content[x] and '<TEXT ' not in content[x]): 
                            x=x+1    
                        #print(x)        
                         
                        while(x<len(content)-1):        
                            f.write(content[x])
                            x=x+1
                        f.write('\n</text> </file>')
                        f.close
                        
                        all_dates.remove(n)
                        break
                        
                        
                    
                
def subcorpus2():
    org_path = r'C:\data\EEBO Phase 1\New folder2'
    extracted_path = r'C:\data\EEBO Phase 1\EEBO Phase 1 letters'
    file_number=0
    #files = os.listdir(org_path)
    all_dates= list(range(1500,1599))
    all_dates.extend(list(range(1500,1701)))
    all_dates.extend(list(range(1500,1701)))
    #all_dates.extend(list(range(1500,1701)))
    #all_dates.extend(list(range(1500,1701)))
    #print(all_dates)

    for path, subdirs, files in os.walk(org_path):
        for filename in files:
            if os.path.splitext(filename)[1] == '.xml':
                file = os.path.join(path, filename)
                #print(file)
                
                #print(file_number)
                
                path_org_file= file
                
                #print(path_org_file)
                
                with open(path_org_file, encoding='utf8') as f:
                    content = f.readlines()
                    
                filename= filename[:-11]
                #print(filename)
                
                for x in range(0, len(content)):
                    while ('<TITLESTMT><TITLE TYPE="' not in content[x]): 
                        x=x+1
                    title= re.findall('">.*?</TITLE>',content[x])[0][2:-8]
                    break
                #print(title)
                if title[-1]=='.':
                    title = title[:-1]
                
                for x in range(0, len(content)):
                    while ('<AUTHOR>' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        author= re.findall('<AUTHOR>.*?</AUTHOR>',content[x])[0][8:-10]
                    else: author='X'
                    break
                #print(author)
                if author == '':
                    author = 'X'
                
                for x in range(10, len(content)):
                    while ('<PUBPLACE>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            place_of_pub= ''
                            break
                    if x !=len(content)-1:
                        place_of_pub= re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
                        break
                    else:
                        break
                #print(place_of_pub)
                place_of_pub = re.sub("[^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]", '', place_of_pub)
                if place_of_pub in ['ImprintedatLondon', 'PrintedatLondon', 'Londini', 'AtLondon', 'ImpryntedatLondon', 'EnpryntedatLondon', 'Londonprinted']:
                    place_of_pub = 'London'
                if place_of_pub in ['PrintedatOxfordieLondon', 'OxfordieLondon']:
                    place_of_pub= 'Oxford and London'
                if place_of_pub =='FrancofortiadMoenum':
                    place_of_pub= 'Frankfurt am Main'
                if place_of_pub =='ImprentitatEdinburgh':
                    place_of_pub= 'Edinburgh'
                
                for x in range(10, len(content)):
                    while ('<DATE>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            pubdate= ''
                            break
                    if x!= len(content)-1:
                        #print(content[x])
                        pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
                        break
                    else:
                        break
                #print(pubdate)
                pubdate = re.sub("[^0123456789]", '', pubdate)
                pubdate = pubdate[-4:]
                
                for x in range(0, len(content)):
                    while ('<IDNO TYPE="stc">' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        idno= re.findall('<IDNO TYPE="stc">.*?</IDNO>',content[x])[0][17:-7]
                        break
                    else: 
                        idno = 'X'
                        break
                #print(idno)
                
                for x in range(10, len(content)):
                    while ('<PUBLISHER>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            publisher= ''
                            break
                    if x !=len(content)-1:
                        publisher= re.findall('<PUBLISHER>.*?</PUBLISHER>',content[x])[0][11:-12]
                        break
                    else:
                        break
                    if publisher[-1] ==',':
                        publisher= publisher[:-1]
                    
                for x in range(0, len(content)):
                    while ('<TERM>' not in content[x]): 
                        x=x+1
                        if x == len(content)-1:
                            keywords= ''
                            break
                    if x !=len(content)-1:
                        keywords= re.findall('<TERM>.*?</TERM>',content[x])[0][6:-7]
                        if keywords[-1] =='.':
                            keywords= keywords[:-1]
                        if keywords=='':
                            keywords='X'
                        break
                    else:
                        break
                
                
                               
                div_flag=0
                for x in range(0, len(content)):
                    while ('<DIV1 TYPE="letter' not in content[x] and '<DIV2 TYPE="letter' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        div_flag=1
                    else: div_flag=0
                    break
                #print(filename)
                #print(div_flag)
                if div_flag:
                    for n in all_dates:
                        if str(n) in pubdate:
    
                            file= os.path.join(extracted_path, str(n)+'_'+str(filename)+'.txt')
                            f= open(file, 'w+', encoding='utf-8')
                            file_number= file_number+1
                            
                            written_header = '<file> <no=%s> <filename=%s> <corpus=EEBO_letters> <title=%s> <author=%s> \
<pubdate=%s> <keywords=%s> <place_of_publication=%s> <publisher=%s> <idno=%s> <encoding=utf-8> <text> \n' %(file_number,filename, title, author, pubdate, keywords, place_of_pub, publisher, idno)
 
                            f.write(written_header)
                            
                            x=0
                            while ('<DIV1 TYPE="letter' not in content[x] and '<DIV2 TYPE="letter' not in content[x]): 
                                x=x+1    
                            #print(x)   
                            f.write(content[x])     
                            x=x+1
                            while('</DIV' not in content[x]):        
                                f.write(content[x])
                                x=x+1
                                if x==len(content):
                                    break
                            if x<len(content):
                                f.write(content[x])
                            f.write('\n</text> </file>')
                            f.close
                            
                            all_dates.remove(n)
                            break

#extract()
subcorpus()
subcorpus2()