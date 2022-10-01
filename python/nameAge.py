from unittest.util import strclass
import time
start_time = time.time()

print("what is your name?")

myName = input()

while myName != "AJ":
    if myName == "your name":
        print("this is not 'your name'. Please type 'your name'?")
        myName = input()

    else:
        print("that is not your name. Please, tell me your real name.")
        myName = input()

print("Hello " + myName + ". That is a good name. How old are you?")

myAge = int(input())
programAge = int(time.time() - start_time)
## input sanitization to convert to an int 
#print(myAge + "? That's funny, I'm only a few seconds old")
#print("I wish I was " + str(int(myAge) * 2) + " years old")

## part of the str forcing
#print("%s? That's funny, I'm only a %s seconds old" %(myAge, programAge))
#print("I wish I was %s years old" % (myAge * 2))

if myAge < 13:
    print("learning young, that's good")

elif myAge == 13:
    print("you're a teenager now... that's cool, I guess")

elif myAge > 13 and myAge < 30:
    print("still yound, still learning...")

elif myAge >= 30 and myAge < 65:
    print("Now you're adulting.")

else:
    print("... you've lived a long time?")



#sleeping the program
time.sleep(3)
print("I'm tired. I go sleep sleep now.")