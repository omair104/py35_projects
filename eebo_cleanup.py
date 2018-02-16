import os, re
g=open(r'C:\data\EEBO Phase 1\plus_words.txt', 'w', encoding='utf-8')
def subcorpus_markup():
    extracted_path = r'C:\data\EEBO Phase 2\EEBO Phase 2 samples'
    cleaned_path =   r'C:\data\EEBO Phase 2\EEBO Phase 2 samples_cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'A07194.txt'
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
                    
            if x!= len(content)-1 and '<TEXT LANG=' in content[x] and 'eng' not in content[x]:
                print(file)
                while 'TEXT>' not in content[x]:
                    x=x+1
                content[x]= '...'
                #print(file)
                #print(content[x])
                #break
                #pass
                    
                    
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
                    
                content[x] = re.sub('▪', '', content[x])
                
            else:
                content[x] = re.sub('unknown', 'X', content[x])
                content[x] = re.sub('<keywords=>', '<keywords=X>', content[x])
                content[x] = re.sub(',>', '>', content[x])
                content[x] = re.sub('\.>', '>', content[x])
                content[x] = re.sub('\?>', '>', content[x])

            
            if '▪' in content[x]:
                #g.write(content[x])
                #g.write('\n')
                
                words = content[x].split()
                for word in words: 
                    if '▪' in word:
                        g.write(file)
                        g.write('\n')
                        g.write(word)
                        g.write('\n')
                #g.write(content[x]) 
                
                
                
            
            f.write(content[x])
            x=x+1
        
        
subcorpus_markup()
        