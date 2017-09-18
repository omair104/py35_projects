import os, re


def initial():
    file = r'H:\circle\text_extractor\new corpus\Innsbruck\org.txt'
    path = r'H:\circle\text_extractor\new corpus\Innsbruck\extracted'
    
    with open(file) as f:
        content = f.readlines()
        
    print(content)
    count = 0
    
    for x in range(0, len(content)):
        if '-------' in content[x]:
            print(x)
            count = count +1
            file = os.path.join(path, str(count)+'.txt')
            f= open(file, 'w+', encoding='utf-8')
            x=x+1
            while '-------' not in content[x]:
                f.write(content[x])
                x=x+1
        
def extract():
    org_path = r'H:\circle\text_extractor\new corpus\Innsbruck\initial'
    extracted_path = r'H:\circle\text_extractor\new corpus\Innsbruck\extracted'
    
    files = os.listdir(org_path)
    file_number=0
    for file in files:
        file_number= file_number+1
        path_org_file= os.path.join(org_path, file)
        
        print(path_org_file)
        
        with open(path_org_file) as f:
            content = f.readlines()
            
        title1= content[18][1:-1]
        title2= content[19][1:][1:-1]
        title=title1+title2
        
        for x in range(0, len(content)):
            while ('<Exact' not in content[x]): 
                x=x+1
            pubdate= content[x][-4:]
            break
        pubdate = re.sub("[^123456789]", '', pubdate)

        
        for x in range(0, len(content)):
            while ('<Author' not in content[x]): 
                x=x+1
            author= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        
        
        for x in range(0, len(content)):
            while ('<Place of author' not in content[x]): 
                x=x+1
            place_author= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Sex of author' not in content[x]): 
                x=x+1
            sex_author= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Status of' not in content[x]): 
                x=x+1
            status_author= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Recipient' not in content[x]): 
                x=x+1
            recipient= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Place of' not in content[x]): 
                x=x+1
            place_recipient= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<SEx of recipient' not in content[x]): 
                x=x+1
            sex_recipient= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<ADdress of' not in content[x]): 
                x=x+1
            address_recipient= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Relation of' not in content[x]): 
                x=x+1
            relation_corr= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Ranks of' not in content[x]): 
                x=x+1
            rank_of= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        for x in range(0, len(content)):
            while ('<Educational' not in content[x]): 
                x=x+1
            educational= re.findall(':.*?\n',content[x])[0][2:-1]
            break

        
        for x in range(0, len(content)):
            while ('<Age' not in content[x]): 
                x=x+1
            authorage= re.findall(':.*?\n',content[x])[0][2:-1]
            print(authorage)
            break
        if '(' in authorage:
            authorage= authorage[-3:-1]
        print(authorage)
        
        for x in range(0, len(content)):
            while ('<Dialect' not in content[x]): 
                x=x+1
            dialect= re.findall(':.*?\n',content[x])[0][2:-1]
            break
        
        
        
        written_header = '<file> <no=%s> <corpus=innsbruck_letter_corpus> <title=%s> <author=%s> <authorage=%s> <dialect=%s> <pubdate=%s> <genre=letter> \
<place of author=%s> <sex of author=%s> <status of author=%s> <recipient=%s> <place of recipient=%s> <sex of recipient=%s> <address of recipient=%s> <relation of correspondents=%s> <ranks of correspondents=%s> <educational background=%s> \
<encoding=utf-8> <text> \n' %(file_number, title, author, authorage, dialect, pubdate, place_author, sex_author, status_author, recipient, place_recipient, sex_recipient, address_recipient, relation_corr, rank_of, educational)
        
        print(written_header)
        
        
        
        file= os.path.join(extracted_path, str(file_number)+'.txt')
        f= open(file, 'w+', encoding='utf-8')
        f.write(written_header)
        
        x=0
        while ('$' not in content[x]): 
            x=x+1           
         
        while(x<len(content)-1):        
            f.write(content[x])
            x=x+1
        f.write('\n</text> </file>')
        f.close
     

        
#initial()
extract()