#guess windows causes errors because it is pulling from another place as well and causing a runtime error, this fixes this. Who would have known
if __name__ == '__main__':

    #This script will use the howdoi module and prompt the user for their question 
    from howdoi import howdoi
    from time import sleep

    print("Please ask you question about anything coding. WARNING, any other types of questions will not work correctly!")

    askedQuestion = input()

    query = askedQuestion

    #getting this to work and finding that this was a possible way to get things to display was fun, its listed in 
    answer = howdoi.howdoi(query)

    print(answer)


#just a little between to not have it jump right to the next
    print("So now that we have that question answered, lets find another question we have using another stack exchange based website")
    sleep(3)
    
    #URL specifying
    print("\nPlease enter the URL of the website you want to use (exclude https://www). \nWARNING, ONLY STACK EXCHANGE BASED WEBSITES WILL WORK")

    #this is what specifies the variable
    HOWDOI_URL=input()

    print("\nNow what is your question?")
    
    askedQuestion = input()

    query = askedQuestion

    answer = howdoi.howdoi(query)

    print(answer)


