#This is the defined function which will gather the information on how many apples and oranges you want to buy and it will compute the total price.
#Inputting non-number characters will render loop to force you to properly input a number.
def totalShoppingSpree():
    while True:
        try:
            myApples = int(input("How many apples do you wish to buy? "))
            myOranges = int(input("How many oranges do you wish to buy? "))
            totalCost = myApples*20 + myOranges*25
            return myApples, myOranges, totalCost
            break
        except:
            print("Please input a proper amount of apples and oranges")
#This is the defined function that will display the returned variables from the previous defined function.
def displayShoppingSpree(applesPara, orangesPara, totalCostPara):
    print(f"{applesPara}*20 + {orangesPara}*25 = {totalCostPara}")
    print(f"The total amount is {totalCostPara} PHP")

#Calling of the two functions with assigned multiple variables for the returned values to be caught.
appleArg, orangeArg, totalCostArg = totalShoppingSpree()
displayShoppingSpree(appleArg, orangeArg, totalCostArg)

#Survey again for the improvement of our shop
while True:
    try:
        rating = int(input("How is your shopping today? Scale from 1 - 5 with 1 being the lowest and 5 being the highest: "))
        if rating == 1:
            print("I am never going back in this garbage shop again!")
            print("We are so sorry")
    
        elif rating == 2:
            print("The shop is overpriced!")
            print("Sorry we can't control SRP")
   
        elif rating == 3:
            print("Meh, it was okay.")
            print("We will do our best to improve the shop!")
    
        elif rating == 4:
            print("This shop looks promising!")
            print("I am glad you appreciate it!")
   
        elif rating == 5:
            print("One of the best shops I have ever went to!")
            print("Thank you very much, please come back again!")

        else:
            error

        break
    except: 
        print("Please enter only numbers from 1 - 5")