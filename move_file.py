import os
import shutil

from_dir= '/Users/vimimutalik/Downloads'
to_dir= '/Applications/Coding Classes/Python/Homework Projects/H102'

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,ext=os.path.splitext(file)
    if (ext==""):
        continue
    if (ext in [".gif",".png",".jpg",".jpeg",".jfif",".avif"]):
        path1=from_dir+"/"+file
        path2=to_dir+"/"+"images"
        path3=to_dir+"/"+"images"+"/"+file
        if (os.path.exists(path2)):
            print("moving...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving...")
            shutil.move(path1,path3)