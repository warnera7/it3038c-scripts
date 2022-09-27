from unittest.util import strclass
import time
start_time = time.time()

print("what is your name?")

myName = input()

print("Hello " + myName + ". That is a good name. How old are you?")

myAge = int(input())
programAge = int(time.time() - start_time)
## input sanitization to convert to an int 
#print(myAge + "? That's funny, I'm only a few seconds old")
#print("I wish I was " + str(int(myAge) * 2) + " years old")

## part of the str forcing
print("%s? That's funny, I'm only a %s seconds old" %(myAge, programAge))
print("I wish I was %s years old" % (myAge * 2))

#sleeping the program
time.sleep(3)
print("I'm tired. I go sleep sleep now.")