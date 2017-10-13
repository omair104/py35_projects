import os, re
def markup():
    extracted_path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted_final_2'
    cleaned_path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file, encoding='utf8') as f:
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
                    #print(content[x])
                    #break
                    pass
                
                f.write(content[x])
                x=x+1
                    
            
            
            
def note_extract():
                
    extracted_path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\cleaned'
    cleaned_path = r'H:\circle\py\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\cleaned2'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= 'D1CCHAPM.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file, encoding='utf8') as f:
            content = f.readlines()
            
        
        
        x=0
        all_notes=''
        while x< len(content):        
            content[x] = re.sub('<note type="address">', '', content[x]) 
            if '<note' in content[x]:
                if '/note>' in content[x]:
                    note = re.findall('<note.*?/note>', content[x])[0]
                    #print(note)
            else: note=''
            all_notes=all_notes+note
            #print(all_notes)
            x=x+1
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x=0
        while x<len(content):
            if x==0:
                content[x]=content[x]+all_notes
            else:
                if '<note' in content[x]:
                    if '/note>' in content[x]:
                        notes = re.findall('<note.*?/note>', content[x])
                        for note in notes:
                            content[x] = re.sub(re.escape(note), '', content[x])
                    else:
                        while '/note>' not in content[x]:
                            x=x+1
                            
            if '/note>' in content[x] and '<note' not in content[x]:
                x=x+1
            else:
                f.write(content[x])   
                   
            if x>2 and '<note' in content[x]:
                print(file)
                #print(content[x])
            
            x=x+1
            
            
        
#initial()
print('Start')
#mid_extracted()
#final_extracted()   
#clean_up()
#markup()

note_extract()