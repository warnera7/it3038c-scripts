# Project 2, Pesky Disk Space
This was all done on a Windows machine, non Windows machines should still work, but there may be errors not seen on a Windows machine.
This is building on my project 1 script.

This script will let you see your total, used and free storage on a drive on your computer, and it can be specified to one of those three outputs, or all of them and in bytes, MB or GB.

Besides giving inputs when prompted, this script runs itself - meaning all you have to do is mess around with your inputs to test it and see what works. 

To run the script, you need python. You do not need to install anything extra. It uses shutil, a module which is installed when you install python.

To be more precise, the script uses shutil.disk_usage to grab overarching storage information about the disc that you will specify and stores it to be used later for conversion or display.

```python
testStorage = shutil.disk_usage(drive)
```
And a while try except loop is used to continually reprompt for an input until a valid drive is specified using the above line of code to validate, this will be something you will be prompted to input. While loops are used to sanitize and confirm that the input is a correct input before the user is prompted for the next.


Normally shutil.disk_usage will give an output showing total, used and free for that drive in bytes. Below is the normal output for a drive using just shutil.disk_usage

![image](https://user-images.githubusercontent.com/111792039/198922639-6f872665-9895-4358-adc3-b494280892f9.png)

This script allows you to choose a single item of the output - total, used or free, or all of them. And it lets you choose if you want them in bytes, megabytes or gigabytes.

This is done through the use of indexes - where 0 is assigned to total, 1 assigned to used and 2 assigned to free, which can then be used individually and converted to your chosen output.

Going in order of what you will see
1. The script will ask you for a drive and reprompt until a valid drive or path is given.
2. Then you will be asked for your preference of how the output will be displayed - bytes, megabytes or gigabytes and prompted until you give a valid response. Feel free to check if the conversions are correct as well if you want to.

THE REQUIRED INPUTS ARE CASE SENSITIVE, they are all lowercase and will reprompt you do upper case sorry :/

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

Here is a picture of an example runthrough of the script, where we display all - total, used and free.

![image](https://user-images.githubusercontent.com/111792039/198923389-787a616e-1275-4faa-bc86-9091b32c2f23.png)

Here is another where we just choose to look at the free amount of space in MB

![image](https://user-images.githubusercontent.com/111792039/198923593-b00583fa-c39c-4ae9-8c35-9d3e2cd75b15.png)


Additionally, due to how the conversions and singular outputs are handled, I use two or three print statements depending and add end="" to the end to force them onto the same lines

```python
print(testStorage[int(chosenspace)], end="")
print(" bytes")
```

  Throughout, all of the accepted inputs are made easily visible and shown again if an inccorect input is given. Additionally, all of the prompts have the choices sent to a new line for easier readibility and so they dont get lost in the text.
