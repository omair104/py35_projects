# -*- coding: utf-8 -*-

import os 

org_path = r'C:\Users\BabriO\Desktop\New corpus\EEBO_samples'
extracted_path = r'C:\Users\BabriO\Desktop\New corpus\all'


files = os.listdir(org_path)
#print(files)
file_number=0
for file in files:
    file_number= file_number+1
    path_org_file= os.path.join(org_path, file)

    
    with open(path_org_file, encoding ='utf-8') as f:
        content = f.readlines()
        
    

    

    x=1
    version = 0
    while(x<len(content)-1):    
        w_file= os.path.join(extracted_path, 'EEBO_samples_'+str(file)[:-4]+'_'+str(version)+'.txt')
        print(w_file)
        f= open(w_file, 'w+', encoding='utf-8')
        line_count=0
        while line_count<40:
            f.write(content[x])
            line_count=line_count+1
            x=x+1
            if x==len(content)-1:
                break
        version=version+1
        f.close
