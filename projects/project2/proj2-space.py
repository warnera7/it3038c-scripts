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


#print(testStorage)
#prints the drive total, used and free in bytes
    # testStorage[0] shows just the total bytes and nothing else - can use this to format it into MB or GB
    # [0:2] for some reason breaks the output