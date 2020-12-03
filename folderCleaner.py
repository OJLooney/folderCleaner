import os
import re
import shutil

filenameRegex = re.compile(r'(.+)\.(.+)')
fileTypes = ["pdf","png","jpeg","txt","docx","jpg","pptx","doc","csv","py","zip","odp","h","cpp"]
directory = "C:\\Users\\Olly_\\Downloads"

def cleanFolder(filenameRegex, fileTypes, directory):
    for filename in os.listdir(directory):
        mo = filenameRegex.search(filename)
        try:
            if(mo.group(2) in fileTypes):
                newDirectory = directory+"\\FolderOf"+mo.group(2)
                if not(os.path.isdir(newDirectory)):  
                    os.mkdir(newDirectory)
                shutil.move(directory+"\\"+filename,newDirectory+"\\"+filename)
        except AttributeError:#sometimes mo = None
            pass