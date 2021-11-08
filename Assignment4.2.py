#This defined function contains a guessing game which you can trigger a 50% discount.
#The discountAct was made global since it will be used in an outside if and else statement.
#The guessing has a limit of 5
def guessingGame():
    discountWord = "Please"
    guessCount = 0
    guessLimit = 5
    guessChance = True
    yourGuess = ""
    global discountAct
    discountAct = False
    while guessChance and discountWord != yourGuess:
        if guessCount < guessLimit:
            yourGuess = input("Guess the secret word, P_e_s_: ")
            guessCount += 1           
        else:
            guessChance = False

    if guessChance:
        print("You won a 50% discount!")
        discountAct = True
    else:
        print("You lost a chance to a discount, the secret word was [Please]")


#This defined function will gather the price of the apple and your current money.
#This will also loop until you correctly input a number not letters.
def allAboutYourShopping():
    while True:
        try:
            applePrice = float(input("What is the price of an apple? "))
            userMoney = float(input("How much money do you possess? "))
            if discountAct:
                applePrice = applePrice*0.50
                apples = userMoney//applePrice
                change = userMoney%applePrice
                return applePrice, userMoney, apples, change
                break
            else:
                apples = userMoney//applePrice
                change = userMoney%applePrice
                return applePrice, userMoney, apples, change
                break
        except:
            print("Please enter duly numerical values.")

#This defined function will display the apples you can buy and your change based on the previous defined function which is allAboutYourShopping().
def displayOutput(applesPara, changePara):
    print(f"You can buy {applesPara} apple(s) and your change is {changePara} PHP.")

#The calling of functions
guessingGame()
applePriceArg, userMoneyArg, applesArg, changeArg = allAboutYourShopping()

#Removing the decimal place again on number of apples you can buy since you can't buy "decimal" number of apples.
applesArg = format(applesArg, '.0f')                                                     
displayOutput(applesArg, changeArg)

