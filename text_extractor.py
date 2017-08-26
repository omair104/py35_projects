import os, time
from collections import defaultdict
data_dict = defaultdict(list)
import numpy as np 

org_file_directory=r'F:\freelance work\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\2510\PCEEC\corpus\txt'
file_name = 'allen.txt'
path_org_file= os.path.join(org_file_directory, file_name)


directory_file = r'F:\freelance work\text_extractor\Parsed Corpus of Early English Correspondence (RAW AND FULL)\\2510\PCEEC\\corpus\\txt\\extracted'


#scan_upto = 'ALLEN'
name = os.path.splitext(file_name)[0]
scan_upto = name.upper()+','
print(scan_upto)

remove_list= ['$', '</paren>' ,'<paren>', '{ED:Englefield}','{ED:Louvain}', '{ED:Owen}', '{ED:Dr._Morys_Clynnog}', '{ED:ADDRESSED_BY_ALLEN:}', 
              '<P_8>','<P_9>', '<P_10>','<P_11>', '<P_12>', '<P_13>', '<P_14>' ,'<P_14>', '<P_15>','<P_16>','<P_17>','<P_18>','<P_19>','<P_73>', '<P_230', 
              '<P_231>','<P_235>',
              '<heading>','</heading>']


with open(path_org_file) as f:
    content = f.readlines()
    

file_names = ()
#dict = {}
for x in range(0, len(content)):
    header = (content[x])
    if header.startswith('AUTHOR'):
        header_1 = header.split(':')
        author_name = header_1[1]
        author_gender= header_1[2]
        author_dob= header_1[4]
        author_age= header_1[5]
        
        header_recipient= content[x+1]
        header_2 = header_recipient.split(':')
        recipient_name = header_2[1]
        recipient_gender= header_2[2]
        recipient_dob= header_2[4]
        recipient_age= header_2[5]
        
        header_letter= content[x+2]
        header_3 = header_letter.split(':')
        letter_name = header_3[1]
        letter_date = header_3[3]
        letter_autograph= header_3[5]
        
        text_start_line = x+3

        
        data_dict[letter_name].append(text_start_line)
        
        
#print(data_dict)

for file_name in data_dict:
    file = os.path.join(directory_file, file_name+'.txt')
    print(file_name)
    print(data_dict[file_name])
    
    f =open(file, 'w+')
    
    header_start = data_dict[file_name][0]-3
    header = content[header_start]
    print(header)
    header_1 = header.split(':')
    author_name = header_1[1].rstrip()
    author_gender= header_1[2].rstrip()
    author_dob= header_1[4].rstrip()
    author_age= header_1[5].rstrip()
    
    
    header_recipient= content[header_start+1]
    header_2 = header_recipient.split(':')
    recipient_name = header_2[1].rstrip()
    recipient_gender= header_2[2].rstrip()
    recipient_dob= header_2[4].rstrip()
    recipient_age= header_2[5].rstrip()
    
    header_letter= content[header_start+2]
    header_3 = header_letter.split(':')
    letter_name = header_3[1].rstrip()
    letter_date = header_3[3].rstrip()
    letter_autograph= header_3[5].rstrip()
    corpus='parsed_corpus_of_early_english_correspondence'
    num=letter_name[-1]
    
    written_header = '<file> <no=%s> <corpusnumber=%s> <corpus=%s> <author=%s> <dialect=bre> <authorage=%s> <pubdate=%s> <genre1=letter> <genre2=X> <encoding=utf-8> <text> \n' %(num, letter_name, corpus, author_name, author_age, letter_date) 
    
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

    
 
