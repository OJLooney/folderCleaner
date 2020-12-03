import os
import re
import shutil


fileTypes = ["pdf","png","jpeg","txt","docx","jpg","pptx","doc","csv","py","zip","odp","h","cpp"]
directory = "C:\\Users\\Olly_\\Downloads"

def cleanFolder(fileTypes, directory):
    #create regex for files
    filenameRegex = re.compile(r'(.+)\.(.+)')

    #loop through files in given directory
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

def getFileTypes():
    size = int(input("Enter how many file types you want to be organised:\n"))
    fileTypes = []
    print("Enter the file types below:\n")
    for i in range(size):
        filetype = input()
        fileTypes.append(filetype)
    print("Done. Thanks!")
    return fileTypes

def getDirectory():
    directory = input("Enter the directory you would like to be organised:\n")

    updatedDirectory = ""
    for i in range(len(directory)):
        if directory[i] == '\\':
            updatedDirectory += "\\"#every '\\' needs a '\' as a flag for later in the program.
        updatedDirectory += directory[i]
    
    return updatedDirectory

directory = getDirectory()
fileTypes = getFileTypes()

cleanFolder(fileTypes, directory)