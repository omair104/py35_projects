import os, re

g=open(r'C:\data\EEBO Phase 1\char_samples_proc.txt', 'w', encoding='utf-8')
def subcorpus_markup():
    extracted_path = r'C:\data\EEBO Phase 1\EEBO TCP Phase 1'
    cleaned_path =   r'C:\data\EEBO Phase 1\EEBO TCP Phase 1_cleaned'
    
    files= os.listdir(extracted_path)
    
    for file in files:
        #file= '1529_A01279.txt'
        path_extracted_file= os.path.join(extracted_path, file)
        
        
        with open(path_extracted_file, encoding='utf-8') as f:
            content = f.readlines()
            
        file= os.path.join(cleaned_path, str(file))
        f= open(file, 'w+', encoding='utf-8')
        
        x= 0
        while x< len(content):
            if '<LANGUAGE' in content[x] and 'eng' not in content[x]:
                y=0
                while '<TEXT LANG=' not in content[y]:
                    y=y+1
                    if y> len(content)-2:
                        #print(file)
                        break
            x=x+1
                    
                        
                
        
        x=0
        while x< len(content):
            '''
            curly_brackets = re.findall('{.*?}', content[x])
            for c in curly_brackets:
                if c not in ['{is}','{us}', '{que}']:
                    print(file)
                    print(c)
            '''

            curly_exceptions = ['{D}', '{d}', '{F}', '{f}', '{g}', '{G}', '{R}', '{r}', '{S}', '{s}', '{T}', '{t}', '{LL}', '{ll}', '{W}', '{w}', '{Y}', '{y}', '{ou}', '{bus}', '{CON}', '{con}', '{er}', '{is}', '{PER}', '{per}', '{pre}', '{pri}', '{PRI}', '{PRO}', '{pro}', '{qu}', '{quam}', '{que}', '{QUE}', '{qui}', '{QUOD}', '{quod}', '{ris}', '{rum}', '{RUM}', '{sed}', '{ser}', '{ur}', '{us}', '{US}', '{es}', '{etc}', '{THAT}', '{that}', '{fj}']
            if any (word in content[x] for word in curly_exceptions):
                pass
            else:
                if '{' in content[x] and '}' in content[x]:

                    curly_brackets = re.findall('{.*?}', content[x])
                    for c in curly_brackets:
                        content[x] = re.sub(re.escape(c), ' ', content[x])
                        
                    g.write(file)
                    g.write(content[x])

            
    
            
            
            if x>0 and x!= len(content)-1:
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
                 
            
            if x!= len(content)-1 and '<TEXT LANG=' in content[x] and 'eng' not in content[x] and 'sco' not in content[x]:
                #print(file)
                while 'TEXT>' not in content[x]:
                    x=x+1
                part2 = content[x].split('TEXT>')[1]
                content[x] = '...'+ part2
                
            '''
            a = re.findall('<ADD.*?ADD>', content[x])
            for b in a:
                g.write(file)
                g.write(b)
                    
            if 'TYPE="modern' in content[x]:
                g.write(file)
                g.write(content[x])
            ''' 
            if 'DIV1 TYPE="modern' in content[x]:
                while '/DIV1' not in content[x]:
                    x=x+1
                    
            content[x] = re.sub('&amp;', '&', content[x])
            if x>0 and x!= len(content)-1:# and '<TEXT L' not in content[x]:
                
                content[x] = re.sub('</SEG>', '', content[x])
                if 'GAP DESC' in content[x]:
                    '''
                    if content[x][-3:-1]=='/>' and content[x+1][:4] == '<GAP':
                        g.write(file)
                        g.write(content[x])
                        g.write(content[x+1])
                    '''
                    gaps = re.findall('<GAP DESC.*?>', content[x])
                    previous_index = 0
                    for gap in gaps:
                        #ending_point = len(gap)
                        length = len(gap)
                        ind = content[x].find(gap, previous_index)
                        #print(content[x])
                        #print(ind,length)
                        if content[x][ind-1] in [' ', '>', '\n'] and content[x][ind+length] in [' ', '<', '\n']:
                            content[x] = re.sub(re.escape(gap), '', content[x],1)
                            #content[x] = re.sub(re.escape(gap), 'EXCEPTION HERE', content[x],1)
                        else:
                            content[x] = re.sub(re.escape(gap), '^', content[x],1)
                        previous_index = ind+1

                
                in_brackets= re.findall('<.*?>',content[x])
                for element in in_brackets:
                    if '>\'s' not in content[x]:
                        content[x] = re.sub(re.escape(element), ' ', content[x])
                    else:
                        content[x] = re.sub(re.escape(element), '', content[x])
                    
                special_characters = ['✿', '❍', '⦾', '★', '●']
                if any (word in content[x] for word in special_characters):
                    
                    content[x] = re.sub('✿', '', content[x])
                    content[x] = re.sub('❍', '', content[x])
                    content[x] = re.sub('⦾', '', content[x])
                    content[x] = re.sub('★', '', content[x])
                    content[x] = re.sub('●', '', content[x])
                    g.write(file)
                    g.write(content[x])
                    
                content[x] = re.sub('∣', '', content[x])
                content[x] = re.sub('¦', '', content[x])
                content[x] = re.sub('¶', '', content[x])
                content[x] = re.sub('❧', '', content[x])
                content[x] = re.sub('☞', '', content[x])
                content[x] = re.sub('❀', '', content[x])
                content[x] = re.sub('☜', '', content[x])
                content[x] = re.sub('\*', '', content[x])
                content[x] = re.sub('✚', '', content[x])
                content[x] = re.sub(':black_small_square:', '', content[x])
                if '=•=' not in content[x]:
                    content[x] = re.sub('•', '', content[x])
                content[x] = re.sub('✿', '', content[x])
                content[x] = re.sub('❍', '', content[x])
                content[x] = re.sub('⦾', '', content[x])
                content[x] = re.sub('★', '', content[x])
                content[x] = re.sub('●', '', content[x])

            
                    
                content[x] = re.sub('▪', '', content[x])
                
            else:
                content[x] = re.sub('unknown', 'X', content[x])
                content[x] = re.sub('<keywords=>', '<keywords=X>', content[x])
                content[x] = re.sub(',> <idno', '> <idno', content[x])
                content[x] = re.sub('\.> <idno', '> <idno', content[x])
                content[x] = re.sub('\?> <idno', '> <idno', content[x])
                content[x] = re.sub('\:> <idno', '> <idno', content[x])
                content[x] = re.sub('\;> <idno', '> <idno', content[x])
                content[x] = re.sub('\]> <idno', '> <idno', content[x])
                content[x] = re.sub('<place_of_publication=EnpryntedinthecyteofLondon>', '<place_of_publication=London>', content[x])
                content[x] = re.sub('<place_of_publication=AtMalborowinthelandeofHesseieAntwerp>', '<place_of_publication=Antwerp>', content[x])
                content[x] = re.sub('<place_of_publication=PrintedatLondonandreprintedatEdinburgh>', '<place_of_publication=London and Edinburgh>', content[x])
                content[x] = re.sub('<publisher=Printed,>', '<publisher=X>', content[x])
                content[x] = re.sub('<publisher=Printed>', '<publisher=X>', content[x])


                
            
            f.write(content[x])
            x=x+1
        
        
subcorpus_markup()
        