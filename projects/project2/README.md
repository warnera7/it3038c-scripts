# Project 2, Pesky Disk Space
This was all done on a Windows machine, non Windows machines should still work, but there may be errors not seen on a Windows machine.

This is building on my project 1 script, the first 19 lines were project 1 and have not been modified, there were 2 additional lines that were previously used to print the variable storing your chosen drive that were removed.

Besides giving inputs when prompted, this script runs itself - meaning all you have to do is mess around with your inputs to test it and see what works. 

To run the script, you need python. You do not need to install anything extra. It uses shutil, a module which is installed when you install python.

To be more precise, the script uses shutil.disk_usage to grab overarching storage information about the disc that you will specify and stores it to be used later for conversion or display.

```python
testStorage = shutil.disk_usage(drive)
```
And a while try except loop is used to continually reprompt for an input until a valid drive is specified using the above line of code to validate, this will be something you will be prompted to input. While loops are used to sanitize and confirm that the input is a correct input before the user is prompted for the next.


Normally shutil.disk_usage will give an output showing total, used and free for that drive in bytes. 


This script allows you to choose a single item of the output - total, used or free, or all of them. And it lets you choose if you want them in bytes, megabytes or gigabytes.

Going in order of what you will see
1. The script will ask you for a drive and reprompt until a valid drive or path is given.
2. Then you will be asked for your preference of how the output will be displayed - bytes, megabytes or gigabytes and prompted until you give a valid response. Feel free to check if the conversions are correct as well if you want to.

```python
print("Would you like your drive space displayed in bytes, megabytes or gigabytes? \n by - for bytes \n mb - for megabytes \n gb - for gigabytes")
desiredoutput = input()
```

3. Last you will be asked what drive information you would like - total, used, free or all and will only accept the listed responses. The formatting of these is different than the normally formatting of the module for better readabilty and showing MB or GB instead of bytes.

```python
print("\nNow would you like total, used or free space displayed?\n 0 - for total \n 1 - for used \n 2 - for free \n 4 - to display all")
chosenspace = input()
```
If you choose bytes, you will get outputs that display the bytes, if you choose megabytes, your output will be converted to megabytes and if you choose gigabytes, the ouput will be converted to gigabytes. Both megabyes and gigabytes are rounded to 2 decimal places.

If you want to remove the rounding, clone the script and remove the round() on any of the MB or GB outputs.

Additionally, due to how the conversions and singular outputs are handled, I use two or three print statements depending and add end="" to the end to force them onto the same lines

```python
print(testStorage[int(chosenspace)], end="")
print(" bytes")
```

  Throughout, all of the accepted inputs are made easily visible and shown again if an inccorect input is given. Additionally, all of the prompts have the choices sent to a new line for easier readibility and so they dont get lost in the text.
