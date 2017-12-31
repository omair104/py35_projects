import os
from collections import defaultdict
import re

def extract():
    directory_file = r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\extracted_new'
    
    org_file_directory=r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\txt'
    
    files = os.listdir(org_file_directory)
    count = 0
    g=open(r'H:\circle\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\number_words.txt', 'w')
    for file in files:
        data_dict = defaultdict(list)
        file_name = file
        #print(file_name)
        #file_name = 'arundel.txt'
        path_org_file= os.path.join(org_file_directory, file_name)
        if os.path.isfile(path_org_file):
        
            
            #scan_upto = 'ALLEN'
            name = os.path.splitext(file_name)[0]
            scan_upto = name.upper()+','

            remove_list= [ '</paren>' ,'<paren>', 
                          '<heading>','</heading>']
            
            #print(path_org_file)
            with open(path_org_file) as f:
                content = f.readlines()
            
            
            x=0
            while x<len(content):
                
                if 'z' in content[x]:# and '{' not in x: #and 'CO' not in x and '@' not in x and '_C' not in x:
                    words = content[x].split()
                    for word in words: 
                        if 'z' in word:
                            g.write(word)


                            g.write('\n')

                '''
                if '-1' in content[x] or '-2' in content[x] or '-3' in content[x] or '-4' in content[x] or '-5' in content[x] or '-6' in content[x] or '-7' in content[x] or '-8' in content[x] or '-9' in content[x]:
                    words = content[x].split()
                    for word in words:
                        if '-1' in word or '-2' in word or '-3' in word or '-4' in word or '-5' in word or '-6' in word or '-7' in word or '-8' in word or '-9' in word:
                            g.write(word)
                            g.write('\n')
                '''
                    

                x=x+1

            '''           
            for x in content:
                a = re.findall('\<P_.*?\>',x)
                if a != []:
                    for element in a:
                        if element not in remove_list:
                            remove_list.append(element)
                        
            #print(remove_list)
                
            #print(len(content))
            for x in range(0, len(content)):
                header = (content[x])
                if header.startswith('AUTHOR'):
                    header_letter= content[x+2]
                    header_3 = header_letter.split(':')
                    
                    header_1 = content[x].split(':')[1]
                    author_first_name = header_1[0:4]
                    letter_name = header_3[1] + '_' + header_3[3][0:4]+ '_' + author_first_name
                    
                    if not any(char.isdigit() for char in header_3[1]):
                        letter_name= header_3[1] + '_'+ header_3[2] + '_' + header_3[3][0:4] + '_' + author_first_name
        
                    text_start_line = x+3
                    data_dict[letter_name].append(text_start_line)
                    
                    
            #print(data_dict)
            for file_name in data_dict:
                file = os.path.join(directory_file, file_name+'.txt')
                
                f =open(file, 'w+')
                
                header_start = data_dict[file_name][0]-3
                #print(header_start)
                header = content[header_start]
                #print(header)
                header_1 = header.split(':')
                #print(header_1)
                author_name = header_1[1].rstrip()
                author_gender= header_1[2].rstrip()
                author_gender=author_gender.lower()
                author_dob= header_1[4].rstrip()
                author_age= header_1[5].rstrip()
                
                
                header_recipient= content[header_start+1]
                header_2 = header_recipient.split(':')
                #print(header_2)
                recipient_name = header_2[1].rstrip()
                recipient_gender= header_2[2].rstrip()
                recipient_dob= header_2[4].rstrip()
                if len(header_2)>5:
                    recipient_age= header_2[5].rstrip()
                else:
                    recipient_age='_'
                
                header_letter= content[header_start+2]
                header_3 = header_letter.split(':')
                #print(header_3)
                letter_name = file_name.rstrip()
                letter_name= letter_name.upper()
                letter_date = header_3[3].rstrip()
                letter_date = re.sub("[^0-9]", "", letter_date)
                letter_autograph= header_3[5].rstrip()
                corpus='parsed_corpus_of_early_english_correspondence'
                num=letter_name[-1]
                
                count = count +1
                author_name= author_name.lower().title()
                author_name= author_name.replace('Iii','III')
                author_name= author_name.replace('Ii','II')
                author_name= author_name.replace('Viii','VIII')
                author_name= author_name.replace('Vii','VII')
                author_name= author_name.replace('Vi','VI')
                author_name= author_name.replace('Iv','IV')
                
                author_name = author_name.replace('_', ' ')
                if author_name=='':
                    author_name='X'
                    
                author_age = re.sub("[^0123456789]", '', author_age)
                if author_age=='':
                    author_age='X'
                if author_gender=='':
                    author_gender='X'
                if letter_date=='':
                    letter_date='X'
                
                written_header = '<file> <no=%s> <filename=%s> <corpus=%s> <author=%s> <authorage=%s> <author_gender=%s> <pubdate=%s> <genre1=letter> <encoding=utf-8> <text> \n' %(count, letter_name, corpus, author_name, author_age, author_gender,letter_date) 
                
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
            '''
            
                

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
            
            content[x] = re.sub(re.escape('{COM:logicall_REPEATED}'), 'logicall', content[x])
            content[x] = re.sub(re.escape('{COM:therefore_repeated}'), 'therefore', content[x])
            content[x] = re.sub(re.escape('{COM:to_REPEATED}'), 'to', content[x])
            content[x] = re.sub(re.escape('{COM:have_REPEATED}'), 'have', content[x])
            content[x] = re.sub(re.escape('{COM:I_REPEATED}'), 'I', content[x])
            content[x] = re.sub(re.escape('{COM:his_repeated}'), 'his', content[x])
            content[x] = re.sub(re.escape('{COM:a_REPEATED}'), 'a', content[x])
            content[x] = re.sub(re.escape('{COM:bee_REPEATED}'), 'bee', content[x])
            content[x] = re.sub(re.escape('{COM:bin_REPEATED}'), 'bin', content[x])
            content[x] = re.sub(re.escape('{COM:so_moche_money_REPEATED}'), 'so moche money', content[x])
            content[x] = re.sub(re.escape('{COM:the_REPEATED}'), 'the', content[x])
            content[x] = re.sub(re.escape('{COM:and_repeated}'), 'and', content[x])
            content[x] = re.sub(re.escape('{ED:as_you_elected_REPEATED}'), 'as you elected', content[x])
            content[x] = re.sub(re.escape('{ED:"for_+t"_REPEATED_IN_MS.} }'), 'for þ', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:1_Pet._3}'), '1 Pet. 3', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:1_Peter_2,_2,_3}'), '1 Peter 2, 2, 3', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:10_Matt.}'), '10 Matt.', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:Chpt._2}'), 'Chpt. 2', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:Ezekiel,_34}'), 'Ezekiel, 34', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:Joan._17}'), 'Joan. 17', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:Matt._10,_v._22}'), 'Matt. 10, v. 22', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:Matt._10,_v._33}'), 'Matt. 10, v. 33', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARGIN:Rom._8}'), 'Rom. 8', content[x])
            content[x] = re.sub(re.escape('{ED:IN_THE_MARHIN:Heb._9}'), 'Heb. 9', content[x])
            content[x] = re.sub(re.escape('{ED:bespeake_WRITTEN_ABOVE_appoint}'), 'bespeake', content[x])
            content[x] = re.sub(re.escape('{ED:ordinary_WRITTEN_ABOVE_table}'), 'ordinary', content[x])
            
            content[x] = re.sub(re.escape('Audoeno {COM:DIAERESIS_ABOVE_THE_LETTER_e_IN_AUDOENO}'), 'Audoëno', content[x])
            content[x] = re.sub(re.escape('the pedacos de historia {COM:A_CEDILLA_ON_LETTER_c_IN_pedacos}'), 'the pedaços de historia', content[x])
            content[x] = re.sub(re.escape('Naive {COM:DIAERESIS_ABOVE_THE_i_IN_Naive}'), 'Naïve', content[x])
            content[x] = re.sub(re.escape('{COM:A_CEDILLA_ON_THE_C_IN_THE_PREVIOUS_WORD}'), '', content[x])
            content[x] = re.sub(re.escape('facon'), 'façon', content[x])
            content[x] = re.sub(re.escape('{COM:DIAERESIS_ABOVE_a_IN_blasd}'), '', content[x])
            content[x] = re.sub(re.escape('blasd'), 'bläsd', content[x])
            content[x] = re.sub(re.escape('have hard'), 'have härd', content[x])
            content[x] = re.sub(re.escape('aboveseid'), 'aböveseid', content[x])

            
            if '{COM:' in content[x] and'}' not in content[x]:
                content[x] = content[x][:-1] + content[x+1]
                content[x+1]=''
            if '{ED:' in content[x] and'}' not in content[x]:
                content[x] = content[x][:-1] + content[x+1]
                content[x+1]=''
            if '{REMOVE:' in content[x] and'}' not in content[x]:
                content[x] = content[x][:-1] + content[x+1]
                content[x+1]=''
                
            if '<em>' in content[x] and'</em>' not in content[x]:
                content[x] = content[x][:-1] + content[x+1]
                content[x+1]=''
            if '<em>' in content[x] and'</em>' not in content[x]:
                content[x] = content[x][:-1] + content[x+2]
                content[x+2]=''
                
                
            
            
                    
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
            
            content[x] = re.sub(re.escape('{to}P'), '', content[x])
            #content[x] = re.sub(re.escape('_P'), '', content[x])
            content[x] = re.sub(re.escape('_MD'), '', content[x])
            content[x] = re.sub(re.escape('<em>'), '', content[x])
            '''
            if '{' in content[x]:
                removes= re.findall('{.*?}', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x]) 
            '''  
            if '{COM' in content[x]:
                removes= re.findall('{COM:.*?}', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x]) 
                    
            if '{ED' in content[x]:
                removes= re.findall('{ED:.*?}', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x]) 
                    
            if '{REMOVE' in content[x]:
                removes= re.findall('{REMOVE:.*?}', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape(remove), '', content[x]) 
                    
                    
            if '{TEXT:' in content[x]:
                removes= re.findall('{TEXT:.*?}', content[x])
                for remove in removes:
                    content[x] = re.sub(re.escape('{TEXT:'), '', content[x])  
                    #content[x] = re.sub(re.escape('}'), '', content[x])  
            
            
            content[x] = re.sub('out_of', 'out of', content[x])
            content[x] = re.sub('{in}_P {her_to_be}', 'in', content[x])
            content[x] = re.sub('{in}_P {that_I_am}', 'in', content[x])
            content[x] = re.sub('{TEXT:through}_P', 'through', content[x])

            content[x] = re.sub(re.escape('_P'), '', content[x])
            
                
            
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
            content[x] = re.sub(' \'s', '\'s', content[x])
            
            content[x] = re.sub('`', '', content[x])
            
            content[x] = re.sub('-1', '', content[x])
            content[x] = re.sub('-2', '', content[x])
            content[x] = re.sub('-3', '', content[x])
            content[x] = re.sub('-4', '', content[x])
            content[x] = re.sub('-5', '', content[x])
            content[x] = re.sub('-6', '', content[x])
            content[x] = re.sub('-7', '', content[x])
            content[x] = re.sub('-8', '', content[x])
            content[x] = re.sub('-9', '', content[x])

            content[x] = re.sub(re.escape('+L'), '$', content[x])
            
            
            content[x] = re.sub(re.escape('+g'), 'ƿ', content[x])
            content[x] = re.sub(re.escape('+G'), 'Ƿ', content[x])
            content[x] = re.sub(re.escape('+t'), 'þ', content[x])
            content[x] = re.sub(re.escape('+T'), 'Þ', content[x])
            content[x] = re.sub(re.escape('+d'), 'ð', content[x])
            content[x] = re.sub(re.escape('+D'), 'Ð', content[x])
            content[x] = re.sub(re.escape('+o'), 'œ', content[x])
            content[x] = re.sub(re.escape('+O'), 'Œ', content[x])
            content[x] = re.sub(re.escape('+a'), 'æ', content[x])
            content[x] = re.sub(re.escape('+A'), 'Æ', content[x])
            
            content[x] = re.sub('yoW', 'yow', content[x])
            content[x] = re.sub('-SBJ', 'yow', content[x])
            
            content[x] = re.sub('{him}', 'him', content[x])
            content[x] = re.sub('{TEXT:ore}', 'ore', content[x])
            content[x] = re.sub('{it}', 'it', content[x])
            content[x] = re.sub('{TEXT:tis}', 'tis', content[x])
            content[x] = re.sub('{TEXT:cannot}', 'cannot', content[x])

            content[x] = re.sub('_ @', '', content[x])
            content[x] = re.sub('_C ODE', '', content[x])
            content[x] = re.sub('_CO DE', '', content[x])
            content[x] = re.sub('_COD E', '', content[x])
            content[x] = re.sub('_C', '', content[x])
            content[x] = re.sub('_CO', '', content[x])
            content[x] = re.sub('_COD', '', content[x])
            content[x] = re.sub('_CODE_X', '', content[x])
            content[x] = re.sub('_CODE_VB', '', content[x])
            content[x] = re.sub('_MD', '', content[x])
            content[x] = re.sub('_CODE_NP', '', content[x])
            content[x] = re.sub('_CODE_NP-OB1', '', content[x])
            content[x] = re.sub('_NP', '', content[x])
            content[x] = re.sub('_NP-SBJ', '', content[x])
            content[x] = re.sub('_NP-OB1', '', content[x])
            content[x] = re.sub('_NP-OB2', '', content[x])
            content[x] = re.sub('_BED', '', content[x])
            content[x] = re.sub('_BE', '', content[x])
            content[x] = re.sub('_BEN', '', content[x])
            content[x] = re.sub('_BEP', '', content[x])
            content[x] = re.sub('_VBD', '', content[x])
            content[x] = re.sub('_NX', '', content[x])
            content[x] = re.sub('_VB', '', content[x])
            content[x] = re.sub('_NEG', '', content[x])
            content[x] = re.sub('_VAN', '', content[x])
            content[x] = re.sub('_CONJ', '', content[x])
            content[x] = re.sub('_ADVP', '', content[x])
            content[x] = re.sub('_HV', '', content[x])
            content[x] = re.sub('{TEXT:cannot}', '', content[x])
            content[x] = re.sub('_VBP', '', content[x])
            content[x] = re.sub('_ADJP', '', content[x])
            content[x] = re.sub('_WNP-3', '', content[x])
            content[x] = re.sub('_EX', '', content[x])
            content[x] = re.sub('_TO', '', content[x])
            content[x] = re.sub('_CODE_NP-POS', '', content[x])
            content[x] = re.sub('_CODE_HVD', '', content[x])
            content[x] = re.sub('_VAG', '', content[x])
            
            
            content[x] = re.sub(re.escape('{COM:SIC?'), '', content[x])
            content[x] = re.sub(re.escape('{COM:??'), '', content[x])
            content[x] = re.sub(re.escape('{COM:?'), '', content[x])
            content[x] = re.sub(re.escape('COMMENCESISMARKEDBYAOINTINGHANDDRAwNINTHEMARGIN}'), '', content[x])
            content[x] = re.sub(re.escape('{COM:THEBEGINNINGIhaveascrupleENDINGbythenextpostwRI'), '', content[x])
            content[x] = re.sub(re.escape('{COM:THEBEGINNINGIhaveascrupleENDINGbythenextpostwRI'), '', content[x])
            content[x] = re.sub(re.escape('{COM:THEBEGINNINGOffHughesENDINGtheytermeitwRITTENINT'), '', content[x])
            content[x] = re.sub(re.escape('{COM:forwrite?'), '', content[x])
            content[x] = re.sub(re.escape('{COM:PASSAGEiijpeereANDENDINGthyngesAlsoscheREPEATE'), '', content[x])
            content[x] = re.sub(re.escape('{COM:thoughnotCANCELLED'), '', content[x])
            content[x] = re.sub(re.escape('{COM:soesooneasperhapsyoudidexpectsentyou'), '', content[x])
            content[x] = re.sub(re.escape('{COM:myCANCELLED'), '', content[x])
            
            if x>1:
                content[x] = re.sub('_', '', content[x])
            else:
                content[x] = re.sub('unknown', 'X', content[x])
            
            if x<len(content)-1 and x>1:
                content[x] = re.sub(re.escape('/'), '', content[x])
                content[x] = re.sub(re.escape('<'), '', content[x])
                content[x] = re.sub(re.escape('>'), '', content[x])
                
            content[x] = re.sub(re.escape('{'), '', content[x])
            content[x] = re.sub(re.escape('}'), '', content[x])
                
            
            if ' W' not in content[x] and x>2:
                content[x] = re.sub('W', 'w', content[x])
            '''
            if '{' in content[x]:
                print('HERE')
                print(content[x])
            '''
            if x>1 and x!= len(content)-1 and ( '{' in content[x] ):
                print(file)
                print(content[x])
                #break
                #pass
            f.write(content[x])
            x=x+1
        
        
    
extract()
#markup()