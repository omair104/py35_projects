import os, re

def subcorpus_markup():
    extracted_path = r'C:\data\EEBO Phase 2\EEBO Phase 2 letters'
    cleaned_path =   r'C:\data\EEBO Phase 2\EEBO Phase 2 letters_cleaned'
    
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
            
            if x>1 and x!= len(content)-1:
                SUP_start= re.findall('<SUP>',content[x])
                for s in SUP_start:
                    content[x] = re.sub(re.escape(s), '=', content[x])
                    
                SUP_end= re.findall('</SUP>',content[x])
                for s in SUP_end:
                    content[x] = re.sub(re.escape(s), '=', content[x])
                    
                    
                
                SUB_start= re.findall('<SUB>',content[x])
                for s in SUB_start:
                    content[x] = re.sub(re.escape(s), '%', content[x])
                    
                SUB_end= re.findall('</SUB>',content[x])
                for s in SUB_end:
                    content[x] = re.sub(re.escape(s), '%', content[x])
                    
                    
                if 'FIGDESC' in content[x]:
                    figdesc= re.findall('<FIGDESC.*?FIGDESC>',content[x])
                    for fig in figdesc:
                        content[x] = re.sub(re.escape(fig), '', content[x])
                    
                    
                    
            content[x] = re.sub('&amp;', '&', content[x])
            if x>0 and x!= len(content)-1:# and '<TEXT L' not in content[x]:
                
                in_brackets= re.findall('<.*?>',content[x])
                for element in in_brackets:
                    content[x] = re.sub(re.escape(element), ' ', content[x])
                    
                content[x] = re.sub('∣', '', content[x])
                content[x] = re.sub('¦', '', content[x])
                content[x] = re.sub('¶', '', content[x])
                content[x] = re.sub('❧', '', content[x])
                content[x] = re.sub('☞', '', content[x])
                content[x] = re.sub(':black_small_square:', '', content[x])
                if '=•=' not in content[x]:
                    content[x] = re.sub('•', '', content[x])
                
            else:
                content[x] = re.sub('unknown', 'X', content[x])

            
            if x>1 and x!= len(content)-1 and '<TEXT LANG=' in content[x] and '<TEXT LANG="eng"' not in content[x]:
                print(file)
                print(content[x])
                #break
                #pass
            
            f.write(content[x])
            x=x+1
        
        
subcorpus_markup()
        