import os
from collections import defaultdict
data_dict = defaultdict(list)


path_to_manual = r'C:\Users\omair\Downloads\hmanual2.1477'
extracted_dir = r'F:\freelance work\text_extractor\XML Helsinki Corpus Browser\XML Helsinki Corpus Browser\hcbrow\corpus\extracted'

files = os.listdir(extracted_dir)
for file in files:
    extracted= os.path.join(extracted_dir, file)
    with open(extracted, encoding='utf-8') as f:
        content = f.readlines()
            
    idno= content[0]
    data_dict[idno].append(file)
    
for idno in data_dict:
    
    idno = '('+idno.rstrip()+')'
    print(idno)


    with open(path_to_manual, encoding='utf-8') as f:
        content = f.readlines()
    
    for x in range(0, len(content)):
        s = content[x].find(idno)
        if s==-1:
            #print('YAAY')
            pass
        else:
            print('NAAAA')
    

