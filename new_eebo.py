# -*- coding: utf-8 -*-
import os,re

def extract():
    org_path = r'C:\data\eebo_original\eebo'
    extracted_path = r'C:\data\eebo_original\extracted'
    file_number=0
    #files = os.listdir(org_path)
    for path, subdirs, files in os.walk(org_path):
        for filename in files:
            if os.path.splitext(filename)[1] == '.xml':
                file = os.path.join(path, filename)
                #print(file)
                
                print(file_number)
                file_number= file_number+1
                path_org_file= file
                
                #print(path_org_file)
                
                with open(path_org_file, encoding='utf8') as f:
                    content = f.readlines()
                    
                filename= filename[:-11]
                print(filename)
                
                for x in range(0, len(content)):
                    while ('<TITLESTMT><TITLE TYPE="' not in content[x]): 
                        x=x+1
                    title= re.findall('">.*?</TITLE>',content[x])[0][2:-8]
                    break
                #print(title)
                
                for x in range(0, len(content)):
                    while ('<AUTHOR>' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        author= re.findall('<AUTHOR>.*?</AUTHOR>',content[x])[0][8:-9]
                    else: author=''
                    break
                #print(author)
                
                for x in range(10, len(content)):
                    while ('<PUBPLACE>' not in content[x]): 
                        x=x+1
                    place_of_pub= re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
                    break
                #print(place_of_pub)
                
                for x in range(10, len(content)):
                    while ('<DATE' not in content[x]): 
                        x=x+1
                    pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
                    break
                #print(pubdate)
                
                for x in range(0, len(content)):
                    while ('<IDNO TYPE="DLPS">' not in content[x]): 
                        x=x+1
                    idno= re.findall('<IDNO TYPE="DLPS">.*?</IDNO>',content[x])[0][18:-7]
                    break
                #print(idno)
                
                
                
                written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=early_english_books_online> <title=%s> <author=%s> <place_of_publication= %s> \
<pubdate=%s> <idno=%s> <encoding=utf-8> <text> \n' %(file_number,filename, title, author, place_of_pub, pubdate, idno)
                
                
                
                file= os.path.join(extracted_path, str(filename)+'.txt')
                f= open(file, 'w+', encoding='utf-8')
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
                
def subcorpus():
    org_path = r'C:\data\eebo_original\eebo'
    extracted_path = r'C:\data\eebo_original\extracted2'
    file_number=0
    #files = os.listdir(org_path)
    all_dates= list(range(1500,1701))
    all_dates.extend(list(range(1500,1701)))
    all_dates.extend(list(range(1500,1701)))
    print(all_dates)

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
                
                for x in range(0, len(content)):
                    while ('<AUTHOR>' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        author= re.findall('<AUTHOR>.*?</AUTHOR>',content[x])[0][8:-9]
                    else: author=''
                    break
                #print(author)
                
                for x in range(10, len(content)):
                    while ('<PUBPLACE>' not in content[x]): 
                        x=x+1
                    place_of_pub= re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
                    break
                #print(place_of_pub)
                
                for x in range(10, len(content)):
                    while ('<DATE' not in content[x]): 
                        x=x+1
                    pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
                    break
                #print(pubdate)
                
                for x in range(0, len(content)):
                    while ('<IDNO TYPE="DLPS">' not in content[x]): 
                        x=x+1
                    idno= re.findall('<IDNO TYPE="DLPS">.*?</IDNO>',content[x])[0][18:-7]
                    break
                #print(idno)
                
                
                
                written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=early_english_books_online> <title=%s> <author=%s> <place_of_publication= %s> \
<pubdate=%s> <idno=%s> <encoding=utf-8> <text> \n' %(file_number,filename, title, author, place_of_pub, pubdate, idno)
                
                for n in all_dates:
                    if str(n) in pubdate:

                        file= os.path.join(extracted_path, str(n)+'_'+str(filename)+'.txt')
                        f= open(file, 'w+', encoding='utf-8')
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
    org_path = r'C:\data\eebo_original\eebo'
    extracted_path = r'C:\data\eebo_original\extracted3'
    file_number=0
    #files = os.listdir(org_path)
    all_dates= list(range(1500,1701))
    all_dates.extend(list(range(1500,1701)))
    all_dates.extend(list(range(1500,1701)))
    all_dates.extend(list(range(1500,1701)))
    all_dates.extend(list(range(1500,1701)))
    print(all_dates)

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
                
                for x in range(0, len(content)):
                    while ('<AUTHOR>' not in content[x]): 
                        x=x+1
                        if x==len(content):
                            break
                    if x<len(content):
                        author= re.findall('<AUTHOR>.*?</AUTHOR>',content[x])[0][8:-9]
                    else: author=''
                    break
                #print(author)
                
                for x in range(10, len(content)):
                    while ('<PUBPLACE>' not in content[x]): 
                        x=x+1
                    place_of_pub= re.findall('<PUBPLACE>.*?</PUBPLACE>',content[x])[0][10:-11]
                    break
                #print(place_of_pub)
                
                for x in range(10, len(content)):
                    while ('<DATE' not in content[x]): 
                        x=x+1
                    pubdate= re.findall('<DATE>.*?</DATE>',content[x])[0][6:-7]
                    break
                #print(pubdate)
                
                for x in range(0, len(content)):
                    while ('<IDNO TYPE="DLPS">' not in content[x]): 
                        x=x+1
                    idno= re.findall('<IDNO TYPE="DLPS">.*?</IDNO>',content[x])[0][18:-7]
                    break
                #print(idno)
                
                
                
                written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=early_english_books_online> <title=%s> <author=%s> <place_of_publication= %s> \
<pubdate=%s> <idno=%s> <encoding=utf-8> <text> \n' %(file_number,filename, title, author, place_of_pub, pubdate, idno)
                
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
                print(filename)
                print(div_flag)
                if div_flag:
                    for n in all_dates:
                        if str(n) in pubdate:
    
                            file= os.path.join(extracted_path, str(n)+'_'+str(filename)+'.txt')
                            f= open(file, 'w+', encoding='utf-8')
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
subcorpus2()