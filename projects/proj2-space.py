import shutil

print("Please enter the path or drive you want to check.")
drive = input()

#method that takes drive checks for drive space, total, used and free
#sanatizes the input and makes sure the input is a drive
while drive != str:
    
    #checks to see if the input is a drive
    try:
        testStorage = shutil.disk_usage(drive)

    #catches when the input is not a drive and continues until it is
    except:
        print("Please enter a valid drive.")
        drive = str(input())
        continue
    break

print("Now would you like total, used or free space displayed?\n 0 - for total \n 1 - for used \n 2 - for free \n 4 - to display all")
chosenspace = input()

while chosenspace != int:
    try:
        if chosenspace == 4:
            print(testStorage)
        
        elif chosenspace == 0 or 1 or 2:
            print(testStorage[int(chosenspace)])

        #doesn't do anything, here on the offchance something goes wrong and it grabs it
        else:
            print("Please enter one of the listed numbers (0, 1, 2 or 4)")
            chosenspace = input()

    except:
        print("please enter one of the listed numbers (0, 1, 2 or 4)")
        chosenspace = input()
        continue
    break

#CAN ALSO ASK IF THEY WANT IT FORMATTED IN BYTES (DONT DO ANYTHING), OR GB AND CAN FORMAT THAT FURTHER BY FEEDING testStorage into another variable




#print(testStorage)
#prints the drive total, used and free in bytes
    # testStorage[0] shows just the total bytes and nothing else - can use this to format it into MB or GB
#print(testStorage[chosenspace])
    # [0:2] for some reason breaks the output