import os
import shutil
from pathlib import Path, WindowsPath, PurePath
from prettytable import PrettyTable
import time


def drivechecker():

    print("Please enter the drive you want to check.")
    userdrive = input()

    #method that takes drive or path and uses that file system to check for drive space, total, used and free
    #sanatizes the input and makes sure the input is a drive
    while userdrive != str:
        
        #checks to see if the input is a drive
        try:
            testStorage = shutil.disk_usage(userdrive)

        #catches when the input is not a drive and continues until it is
        except:
            print("Please enter a valid drive.")
            userdrive = str(input())
            continue
        break


    print("Would you like your drive space displayed in bytes, megabytes or gigabytes? \n by - for bytes \n mb - for megabytes \n gb - for gigabytes")
    desiredoutput = input()

    #sanitizing the input, little wonky but works
    while not desiredoutput in ("by", "mb", "gb"):
        print("Please enter one of the display choices - by or mb or gb")
        desiredoutput = input()
        continue


    print("\nNow would you like total, used or free space displayed?\n 0 - for total \n 1 - for used \n 2 - for free \n 4 - to display all")
    chosenspace = input()

    while chosenspace == 0 or 1 or 2 or 4:
        try:
            if chosenspace == str(4):
                if desiredoutput == "by":
                    
                    #this isnt needed, but i wanted to have the same formatting across the board
                    print("Total: ", end="")
                    print((testStorage[0]), end="")
                    print(" bytes")

                    print("Used: ", end="")
                    print((testStorage[1]), end="")
                    print(" bytes")

                    print("Free: ", end="")
                    print((testStorage[2]), end="")
                    print(" bytes")

                
                elif desiredoutput == "mb":
                    #MBStorage = (testStorage[0] / 1048576), (testStorage[1] / 1048576), (testStorage[2] / 1048576) 

                    #these arent pretty but they work and dont throw errors, for some reason stashing and rounding causes an error and breaks the code 
                    print("Total: ", end="")
                    print(round(testStorage[0] / 1048576, 2), end="")
                    print(" MB")

                    print("Used: ", end="")
                    print(round(testStorage[1] / 1048576, 2), end="")
                    print(" MB")

                    print("Free: ", end="")
                    print(round(testStorage[2] / 1048576, 2), end="")
                    print(" MB")


                elif desiredoutput == "gb":
                    #GBStorage = (testStorage[0] / 1073741824), (testStorage[1] / 1073741824), (testStorage[2] / 1073741824)
                    
                    print("Total: ", end="")
                    print(round(testStorage[0] / 1073741824, 2), end="")
                    print(" GB")

                    print("Used: ", end="")
                    print(round(testStorage[1] / 1073741824, 2), end="")
                    print(" GB")

                    print("Free: ", end="")
                    print(round(testStorage[2] / 1073741824, 2), end="")
                    print(" GB")


            elif chosenspace == 0 or 1 or 2:
                #maybe for project 3 could make it so it reads the input and applies what they are in front
                if desiredoutput == "by":
                    print(testStorage[int(chosenspace)], end="")
                    print(" bytes")
                
                elif desiredoutput == "mb":
                    MBStorage = testStorage[int(chosenspace)] / 1048576
                    print(round(MBStorage, 2), end="")
                    print(" MB")
                
                elif desiredoutput == "gb":
                    GBStorage = testStorage[int(chosenspace)] / 1073741824
                    print(round(GBStorage, 2), end="")
                    print(" GB")
                

            #doesn't do anything, here on the offchance something goes wrong and it grabs it
            else:
                print("please enter one of the listed numbers (0, 1, 2 or 4)")
                chosenspace = input()

        except:
            print("Please enter one of the listed numbers (0, 1, 2 or 4)")
            chosenspace = input()
            continue
        break

def filefinder():
    print("What directory/path would you like to check for files and their sizes?")
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

    #sanitising the extension input by checking the length of the variable list - to see if it has data or is empty
    while len(ex) == 0:
        try:
            #reprompting to allow the variable to change and a working extension to be accepted
            print("There are no files with this extension, please enter another.")
            fextension = input()
            ex = sorted(Path(givenPath).glob('*' + fextension))
            continue

        except:
            print("you shouldn't be here")
        break

    #code snippet inspired by https://zetcode.com/python/pathlib/ and their PrettyTable example        
    prettab = PrettyTable()
    prettab.field_names = ["File name", "Size (MB)"]

    #alligns the data and headings 
    prettab.align["File name"] = "l"
    prettab.align["Size (MB)"] = "r"

    #loop to get the files with their names and sizes
    for x in p.glob('**/*' + fextension):

        size = x.stat().st_size
        sizeMB = round(size / 1024, 2) 
        prettab.add_row([x.name, sizeMB])

    #for sorting the data instead of it just being all thrown in
    print("\nSort by name or by size? \nname - sort by name, or size - sort by size")
    pretSort = input()
      
    #sorts in ascending order
    if pretSort == "name":
        print(prettab.get_string(sortby="File name"))
    elif pretSort == "size":
        print(prettab.get_string(sortby="Size (MB)"))
    else:
        print('Please enter "name" or "size" to sort the output')
        pretSort = input()

        
#this block is calling the functions based on what the user asks to use
runWhat = ""

while runWhat != str:
    
    print("Would you like the drive space checker, filefinder/file size or both? \ndrivr - for drive, \nfindr - for file finder \nboth - for both")
    runWhat = input()
    try:
        if runWhat == 'drivr':
            drivechecker()

        elif runWhat == 'findr':
            filefinder()

        #runs both parts and has a timer delay between to allow you to see the result of the first
        elif runWhat == 'both':
            drivechecker()
            time.sleep(2)
            filefinder()
        
        else:
            print("is this working")
            continue

    except:
        print("That is not a valid choice, please enter one of the responses. \ndrivr - for drive, \nfindr - for file finder \nboth - for both, test ")
        runWhat = input()
        continue
    break