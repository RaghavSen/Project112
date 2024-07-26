import os 
import shutil

from_dir = "c:/Users/BHUVNESH/Downloads"
to_dir = "c:/Users/BHUVNESH/Desktop"

list_of_files = os.listdir(from_dir)

for filename in list_of_files:
    name,extension = os.path.splitext(filename)
    
    if extension == '':
        continue
    if extension in ['.pdf']:
        path1 = from_dir + '/' + filename
        path2 = to_dir + '/' + 'PyFiles'
        path3 = to_dir + '/' + 'PyFiles' + '/' + filename
        
        if os.path.exists(path2):
            print("Moving" + filename)
            shutil.move(path1,path3)
            
        
        else:
            os.makedirs(path2)
            print("Moving" + filename)
            shutil.move(path1,path3)    