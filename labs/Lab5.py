from ast import For, Num
import random


print("Guess an integer between 1 and 1000. (Option 4)")

CorrectNum = random.randrange(1,1000)

#getting the users input
GuessNum = int(input())
#easy way to see if it was working right
#print(CorrectNum)

while GuessNum != CorrectNum:
    #making sure that 0 > number < 1001 is not run through the list
    if  GuessNum > 1000 or GuessNum < 1:
        print("Please enter a number between 1 and 1000.")
        GuessNum = int(input())
    
    elif GuessNum > CorrectNum:
        print("You guessed too high, guess lower.")
        GuessNum = int(input())
    
    elif GuessNum < CorrectNum:
        print("You guessed too low, guess higher.")
        GuessNum = int(input())

    else:
        print("Please enter a number.")
        GuessNum = int(input())
#allows for CorrectNum to be an int but also a string through conversion
print("You guessed it, the number was " + str(int(CorrectNum)) + "!")

#I was having a ton of trouble sanatising the input to int only if you were feeding it a string without it getting stuck as a string or throwing an error, so lets just ignore that