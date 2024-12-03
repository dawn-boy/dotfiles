import os, shutil, sys

def renamer(fullPath,start=0):

    tempPath= fullPath+"/temp/"
    os.mkdir(tempPath)
    count = int(start)

    for path in os.scandir(fullPath):
        if path.is_file():
            shutil.copy2(path.path,tempPath+f"{count}.jpg")
            count+=1
            
path = "/home/Dew/Pictures/walls/new"

if len(sys.argv) > 2:
    renamer(sys.argv[1],sys.argv[2])
else:
    print(f"Provide arguments.\n\npython {sys.argv[0]} [path] [startNum]")
