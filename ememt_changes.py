import os, re

extracted_path = r'H:\circle\text_extractor\changes\EMEMT_new\EMEMT_new'
cleaned_path = r'H:\circle\text_extractor\changes\EMEMT_new\cleaned'

files= os.listdir(extracted_path)

for file in files:
    #file= 'D1CCHAPM.txt'
    path_extracted_file= os.path.join(extracted_path, file)
    
    
    with open(path_extracted_file, encoding='utf-8') as f:
        content = f.readlines()
        
    file= os.path.join(cleaned_path, str(file))
    f= open(file, 'w+', encoding='utf-8')
    
    x=0
    while x< len(content):
        
        
        if x>1:
            content[x] = re.sub('w~', 'w\'', content[x])
            content[x] = re.sub('k~', 'k\'', content[x])
            content[x] = re.sub('<text>', '</text>', content[x])
            content[x] = re.sub('<file>', '</file>', content[x])
        else:
            content[x] = re.sub('<author=>', '<author=X>', content[x])
            content[x] = re.sub('<author=unknown>', '<author=X>', content[x])
            content[x] = re.sub('Attributed to', '', content[x])
            content[x] = re.sub(re.escape('['), '', content[x])
            content[x] = re.sub(re.escape(']'), '', content[x])
            content[x] = re.sub(re.escape('.>'), '>', content[x])
            
            content[x] = re.sub('>  <', '> <', content[x])
            content[x] = re.sub('Attributed to', '', content[x])
            content[x] = re.sub('Attributed to', '', content[x])
            content[x] = re.sub('Attributed to', '', content[x])
            
            content[x] = re.sub('anonymous', 'X', content[x])
            content[x] = re.sub('Anonymous', 'X', content[x])
            content[x] = re.sub('ȝ', '3', content[x])
            

            
    
        

        f.write(content[x])
        x=x+1
