import os,re

def extract():
    org_path = r'H:\circle\text_extractor\new corpus\Newsbooks\The Lancaster Newsbooks Corpus (17th century)\2531\all'
    extracted_path = r'H:\circle\text_extractor\new corpus\Newsbooks\The Lancaster Newsbooks Corpus (17th century)\2531\extracted'
    
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
        
        
        written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=lancaster_newsbook_corpus> <title=%s> \
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
    