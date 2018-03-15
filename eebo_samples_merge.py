import os

folder_location = r'C:\data\EEBO Phase 1 samples_cleaned'


files= os.listdir(folder_location)

'''
years_done = []
for file in files:
    print(file)
    year = file[0:4]
    file_info = os.stat(os.path.join(folder_location, file))
    size = file_info.st_size
    print(size)
    
    
    if year not in years_done and int(year)%2==1 or ( int(year)%3==1 and size<30000):
        years_done.append(year)
        
    else:
        #pass
        os.remove(os.path.join(folder_location, file))
    
#print(years_done)




'''

for file in files:
    os.rename(os.path.join(folder_location, file), os.path.join(folder_location, file)[:-4] + '_P1.txt')
    
