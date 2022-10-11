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

#prints the drive total, used and free in bytes
print(testStorage)