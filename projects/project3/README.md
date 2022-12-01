# Project 3, Pesky Disk Space and Filefinder/Filesizer

### **You will need to install prettytable to get part 2 (findr) to display correctly. Part 1 (drivr) will work without it still.**

**Proj3.space is the file you need to download and run, the other file is just to show a little bit of my thinking for getting the part 2 functionality and basic version of it working.**

This was all done on a Windows machine, non Windows machines should still work, but there may be errors not seen on a Windows machine.
This is building on my project 2 script.

Part 1 and Part 2 are set in different functions that are later then called at the bottom of the code by the variable "runWhat". Based on the value of "runWhat", you can call the drive checking function, the filefinder/filesize function or both. 

## Part 1, Pesky Disk Space

This script will let you see your total, used and free storage on a drive on your computer, and it can be specified to one of those three outputs, or all of them and in bytes, MB or GB.

Besides giving inputs when prompted, this script runs itself - meaning all you have to do is mess around with your inputs to test it and see what works. 

To run the script, you need python. It uses shutil, a module which is installed when you install python.

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


## Part 2 Filefinder/Filesizer

### If you havent already, you need to install PrettyTable, can be done using the command: 
```python
pip install prettytable
```

**Due to how it is set up, setting the path to a directory with only folders and no file will not display results**

Part 2 uses the python module pathlib and its Path function to do most of the routing for files. It additionally uses PrettyTable to help display the returned results in an easier to read output. os is also used to sanatize the input for the path, tried to get it working with a pathlib function/arg but none seemed to work as well as os.path.getsize.

Here is a sample run of the file finder part

![image](https://user-images.githubusercontent.com/111792039/205000677-eabf2694-04e8-4b5f-8e44-206249172a13.png)



We first start off by asking for a path to pointed towards, where we can then find files and we validate that to make sure it is a valid path.

Then using the Path.glob method we ask for a file extension to be searched for in the already specified path. We also validate that the extension we are given is found within that path and if it is not, we ask again for an extension to search for. 

After getting a valid file extension, the files are stored and the PrettyTable is built with a File name and Size (MB) headers. The data is also alligned to make it easier to read.

A for loop using the previously input path along with .glob('**/*') and the specified filed extension to determine the sizes of the files. I also divided the values by 1024 to get it display in megabytes and rounded to two decmimals.

Next we have a choice of sorting the returned files either by name or size, which is another input given and it is sorted in ascending order.


At the end of the file is the variable "runWhat" which is used to allow users to run one of the functions, or both one after the other with a sleep timer of 2 to give you a chance to read the output of the first. This is done with a while try: except: loop with nested if and elif statements.



## Project Usefulness and Challenges

I wanted to make something that could be used instead of looking at the file explorer and show you data that you might have to look in multiple places all in one. With the drive space part, I was looking for something different and it caught my attention. Plus who doesn't like being able to see how much space we actually have on our drives before rounding (even though I did round) and how much is being used by what.

For the second part of the project, I originally wanted to go with a filefinder with a user specified size but couldn't seem to get it to work in the way I wanted when I was trying to use os and os.path and os.walk and feeding them inputs. Instead I pivoted to more a file searching with the size attached and the ability to specify the extension you wanted to find. 

Being able to specify the extension was something that I found interesting and useful for people who have way too many files sitting in a folder and dont want to have to change the sort settings in the file explorer when they want a certain type of file. Also I just wanted to do something a different way just because it sounded interesting to see a little of what a very very basic version of a file explorer would look like and how it would function.

A huge challenge for this project was os and os.path to where I pivoted to pathlib and Path and it was much easier to work with. 
Another challenge was sanitizing inputs and making sure that if an incorrect input was given, the user could keep going until they gave the correct one or quit the program. I am not sure why it was such a problem for me this time around, since it was not anything super special but my brain just did not connect with some of the ways to sanitize the inputs or why it was only partially working.

