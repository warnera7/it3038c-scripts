import os
import pprint
from pathlib import Path, WindowsPath, PurePath

print("give path pls")
givenPath = input()

#getting the path
p = Path(givenPath)


while givenPath != str:
    #making sure it is a valid path/drive to be checked
    try:
        #nothing within pathlib was working to validate it was there without it being an infinite except loop
        sizecheck = os.path.getsize(givenPath)

    #reprompting if given an something not valid
    except:
        print("please enter a valid path")
        givenPath = input()
        continue
    break

print("what file extension would you like to search for in the path? (ex. .py)")
fextension = input()

#finding items with the same extensions in the path
ex = sorted(Path(givenPath).glob('*' + fextension))

#sanitising the extension input by checking the length of the variable it is used in
while len(ex) == 0:
    try:
        print("There are no files with this extension, please enter another.")
        fextension = input()
        ex = sorted(Path(givenPath).glob('*' + fextension))
        continue

    except:
        print("you shouldn't be here")
    break
        

# #gives child item of specified path
# for child in p.iterdir(): child

#doing this to make it easier to read the files
pprint.pp(ex)
#size of that given path



