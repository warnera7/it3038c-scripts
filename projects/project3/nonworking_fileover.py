import os
from os import walk
from os.path import join, isfile, isdir

#it wont work and i cant figure out loading values into other functions
#class userInput:

print("give path pls")
givenPath = input()

while givenPath != str:
    #making sure it is a valid path/drive to be checked
    try:
        sizecheck = os.path.getsize(givenPath)

    #reprompting if given an something not valid
    except:
        print("please enter a valid path")
        givenPath = input()
        continue
    break


print("larger than what size in MB")
filesizeMB = int(input())

filesizeBytes = (filesizeMB * 1048576)



class filefindersize:

    def __init__(self) -> None:
        pass

    #getting the files from the path and those over specified size
    def files_larger_than(givenPath, size):
        
        #throwing the files into a iterable list
        foundFiles = []

        for root, dirs, files in os.walk(path):
            for file in dirs:
                path = os.path.join(root, file)

                if os.path.getsize(path) > size:
                    foundFiles.append(path)
                    
        return foundFiles
    files_larger_than()