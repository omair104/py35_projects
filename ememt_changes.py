import os, re

extracted_path = r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT_marco\EMEMT'
cleaned_path = r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT_marco\cleaned'

g=open(r'H:\circle\text_extractor\new corpus\EMEMT\EMEMT_marco\nepe.txt', 'w', encoding='utf-8')

files= os.listdir(extracted_path)

for file in files:
    #file= 'D1CCHAPM.txt'
    path_extracted_file= os.path.join(extracted_path, file)
    
    
    with open(path_extracted_file, encoding='utf-8') as f:
        content = f.readlines()
        
    file2= os.path.join(cleaned_path, str(file))
    h= open(file2, 'w+', encoding='utf-8')
    
    x=0
    while x< len(content):
        
        
        if x>1:
            
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
            
            
            content[x] = re.sub('Æ~', 'Ǣ', content[x])
            content[x] = re.sub('æ~', 'ǣ', content[x])
            content[x] = re.sub('B~', 'B̄', content[x])
            content[x] = re.sub('b~', 'b̄', content[x])
            content[x] = re.sub('C~', 'C̄', content[x])
            content[x] = re.sub('c~', 'c̄', content[x])
            content[x] = re.sub('D~', 'D̄', content[x])
            content[x] = re.sub('d~', 'd̄', content[x])
            content[x] = re.sub('G~', 'Ḡ', content[x])
            content[x] = re.sub('g~', 'ḡ', content[x])
            content[x] = re.sub('J~', 'J̄', content[x])
            content[x] = re.sub('j~', 'j̄', content[x])
            content[x] = re.sub('K~', 'K̄', content[x])
            content[x] = re.sub('k~', 'k̄', content[x])
            content[x] = re.sub('M~', 'M̄', content[x])
            
            content[x] = re.sub('m~', 'm̄', content[x])
            content[x] = re.sub('N~', 'N̄', content[x])
            
            content[x] = re.sub('n~', 'n̄', content[x])
            
            content[x] = re.sub('P~', 'P̄', content[x])
            content[x] = re.sub('p~', 'p̄', content[x])
            content[x] = re.sub('Q~', 'Q̄', content[x])
            content[x] = re.sub('q~', 'q̄', content[x])
            
            content[x] = re.sub('R~', 'R̄', content[x])
            content[x] = re.sub('r~', 'r̄', content[x])
            content[x] = re.sub('S~', 'S̄', content[x])
            content[x] = re.sub('s~', 's̄', content[x])
            content[x] = re.sub('T~', 'T̄', content[x])
            content[x] = re.sub('t~', 't̄', content[x])
            content[x] = re.sub('W~', 'W̄', content[x])
            content[x] = re.sub('w~', 'w̄', content[x])
            content[x] = re.sub('X~', 'X̄', content[x])
            content[x] = re.sub('x~', 'x̄', content[x])
            content[x] = re.sub('Z~', 'Z̄', content[x])
            content[x] = re.sub('z~', 'z̄', content[x])

            content[x] = re.sub('~', 'ō', content[x])

            content[x] = re.sub(re.escape('brou3t'), 'brouȝt', content[x])
            content[x] = re.sub(re.escape('Li3arde'), 'Liȝarde', content[x])
            content[x] = re.sub(re.escape('mi3t'), 'miȝt', content[x])
            content[x] = re.sub(re.escape('ne3e'), 'neȝe', content[x])
            content[x] = re.sub(re.escape('neƿe'), 'neȝe', content[x])
            content[x] = re.sub(re.escape('practi3e'), 'practiȝe', content[x])
            content[x] = re.sub(re.escape('ri3t'), 'riȝt', content[x])
            
            
            content[x] = re.sub(re.escape('+e'), 'e', content[x])
            content[x] = re.sub(re.escape('+pit'), 'pit', content[x])
     

            
    
        

        h.write(content[x])
        x=x+1
