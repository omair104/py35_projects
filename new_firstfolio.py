import os,re

def markup():
    extracted_path = r'H:\circle\py\new corpus\FirstFolio\Shakespeare First Folio (Machine Readable Text Format)\extracted'
    cleaned_path = r'H:\circle\py\new corpus\FirstFolio\Shakespeare First Folio (Machine Readable Text Format)\cleaned'
    
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
            
            if '<P' in content[x]:
                x=x+1

            
            else:
                if x>1:
                    content[x] = re.sub('_', '', content[x])
                content[x] = re.sub('{', '', content[x])
                content[x] = re.sub('}', '', content[x])
                content[x] = re.sub('<S', '', content[x])
                content[x] = re.sub('<P', '', content[x])
                content[x] = re.sub('<D', '', content[x])
                content[x] = re.sub('<Z', '', content[x])
                
                content[x] = re.sub('-', '', content[x])
                content[x] = re.sub('#-', '-', content[x])
                content[x] = re.sub('#', '', content[x])
                content[x] = re.sub('%', '-', content[x])
                content[x] = re.sub('\*', '', content[x])
                content[x] = re.sub('|', '', content[x])
                
                content[x] = re.sub('|', '', content[x])
                content[x] = re.sub(re.escape('('), '', content[x])
                
                content[x] = re.sub('genre1', 'genre', content[x])
                
                if x==0 or x==len(content)-1:
                    f.write(content[x])
                else:
                    content[x] = re.sub('>', '', content[x])
                    f.write(content[x][4:])
                x=x+1
#extract()        
markup()