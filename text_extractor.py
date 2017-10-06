import os
from collections import defaultdict
import re

def extract():
    directory_file = r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\extracted_new'
    
    org_file_directory=r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\txt'
    
    files = os.listdir(org_file_directory)
    print(files)
    
    for file in files:
        data_dict = defaultdict(list)
        file_name = file
        print(file_name)
        #file_name = 'arundel.txt'
        path_org_file= os.path.join(org_file_directory, file_name)
        if os.path.isfile(path_org_file):
        
            
            #scan_upto = 'ALLEN'
            name = os.path.splitext(file_name)[0]
            scan_upto = name.upper()+','
            
            
            
            
            remove_list= [ '</paren>' ,'<paren>', 
                          #'{ED:Englefield}','{ED:Louvain}', '{ED:Owen}', '{ED:Dr._Morys_Clynnog}', '{ED:ADDRESSED_BY_ALLEN:}', '{ED:1593}',
                          #'{ED:Griffin}', '{ED:Maastricht}', '{ED:Thomas}', '{ED:Richard}', '{ED:Paris}', '{ED:P.S.}', '{ED:ow}', '{ED:SIC}',
                          #'<P_8>','<P_9>', '<P_10>','<P_11>', '<P_12>', '<P_13>', '<P_14>' ,'<P_14>', '<P_15>','<P_16>','<P_17>','<P_18>','<P_19>','<P_73>', '<P_230', 
                          #'<P_231>','<P_235>',
                          '<heading>','</heading>']
            
            
            with open(path_org_file) as f:
                content = f.readlines()
            
            
            for x in content:
                a = re.findall('\{ED:.*?\}',x)
                if a != []:
                    for element in a:
                        if element not in remove_list:
                            remove_list.append(element)
                            
            
            for x in content:
                a = re.findall('\<P_.*?\>',x)
                if a != []:
                    for element in a:
                        if element not in remove_list:
                            remove_list.append(element)
                        
            print(remove_list)
                
            print(len(content))
            for x in range(0, len(content)):
                header = (content[x])
                if header.startswith('AUTHOR'):
                    header_letter= content[x+2]
                    header_3 = header_letter.split(':')
                    letter_name = header_3[1]
        
                    text_start_line = x+3
                    data_dict[letter_name].append(text_start_line)
                    
                    
            print(data_dict)
            
            for file_name in data_dict:
                file = os.path.join(directory_file, file_name+'.txt')
                
                f =open(file, 'w+')
                
                header_start = data_dict[file_name][0]-3
                print(header_start)
                header = content[header_start]
                print(header)
                header_1 = header.split(':')
                print(header_1)
                author_name = header_1[1].rstrip()
                author_gender= header_1[2].rstrip()
                author_dob= header_1[4].rstrip()
                author_age= header_1[5].rstrip()
                
                
                header_recipient= content[header_start+1]
                header_2 = header_recipient.split(':')
                print(header_2)
                recipient_name = header_2[1].rstrip()
                recipient_gender= header_2[2].rstrip()
                recipient_dob= header_2[4].rstrip()
                if len(header_2)>5:
                    recipient_age= header_2[5].rstrip()
                else:
                    recipient_age='_'
                
                header_letter= content[header_start+2]
                header_3 = header_letter.split(':')
                print(header_3)
                letter_name = header_3[1].rstrip()
                letter_date = header_3[3].rstrip()
                letter_autograph= header_3[5].rstrip()
                corpus='parsed_corpus_of_early_english_correspondence'
                num=letter_name[-1]
                
                written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=%s> <author=%s> <authorage=%s> <pubdate=%s> <genre1=letter> <encoding=utf-8> <text> \n' %(num, letter_name, corpus, author_name, author_age, letter_date) 
                
                f.write(written_header+ '\n')
                
                
                for start_line in data_dict[file_name]:
                    
                    #print(content[start_line-3])
                    #print(start_line)
                    
                    while(scan_upto not in content[start_line]):
                        filtered_line = content[start_line]
                        for remove_element in remove_list:
                            filtered_line=filtered_line.replace(remove_element,'')
            
                        f.write(filtered_line)
                        start_line = start_line+1
                        
                    #print(content[start_line].rsplit(scan_upto, 1)[0])
                    
                    filtered_line = content[start_line]
                    for remove_element in remove_list:
                        filtered_line=filtered_line.replace(remove_element,'')
                    f.write(filtered_line.rsplit(scan_upto, 1)[0])
                    f.write('\n')
                    
                footer = '\n</text> </file>'
                f.write(footer)
                
                f.close()
            
                

def markup():
    extracted_path = r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\extracted_new'
    cleaned_path = r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\cleaned'
    
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
            
            if '{TEXT:' in content[x]:
                removes= re.findall('{TEXT:.*?}', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape('{TEXT:'), '', content[x])  
                    content[x] = re.sub(re.escape('}'), '', content[x])  
                    
            if '$' in content[x]:
                #print(content[x])
                removes= re.findall('\$.*?\s', content[x])
                #print(removes)
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x])   
                    
            if '<em' in content[x]:
                #print(content[x])
                removes= re.findall('<em.*?/em>', content[x])
                #print(removes)
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x])   
            


            if x>1:
                content[x] = re.sub('_', '', content[x])
            else:
                content[x] = re.sub('unknown', 'X', content[x])
                
            content[x] = re.sub(re.escape('/'), '', content[x])
            content[x] = re.sub('    <dialect=Early Modern English>', '', content[x])
            content[x] = re.sub('<genre2=X>', '', content[x])
            content[x] = re.sub('<genre1', '<genre', content[x])
            
            content[x] = re.sub(' \'d', '\'d', content[x])
            content[x] = re.sub('<font>', '', content[x])
            content[x] = re.sub('<font>', '', content[x])
            content[x] = re.sub('<font>', '', content[x])
            content[x] = re.sub('<font>', '', content[x])

            
            
            


            
            content[x] = re.sub('<font>', '', content[x])
            content[x] = re.sub('</font>', '', content[x])
            content[x] = re.sub('<dialogue>', '', content[x])
            content[x] = re.sub('</dialogue>', '', content[x])
            content[x] = re.sub('<nonSpeech>', '', content[x])
            content[x] = re.sub('</nonSpeech>', '', content[x])
            content[x] = re.sub('<font>', '', content[x])
            content[x] = re.sub('</font>', '', content[x])
            content[x] = re.sub('<head>', '', content[x])
            content[x] = re.sub('</head>', '', content[x])
            content[x] = re.sub('<foreign>', '', content[x])
            content[x] = re.sub('</foreign>', '', content[x])
            content[x] = re.sub('</sample>', '', content[x])
            content[x] = re.sub('<emendation>', '', content[x])
            content[x] = re.sub('</emendation>', '', content[x])

            
            
            if x>1 and x!= len(content)-1 and '$' in content[x]:
                print(content[x])
                #break
                #pass
            f.write(content[x])
            x=x+1
        
        
    
#extract()
markup()
