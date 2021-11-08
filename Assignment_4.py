#The defined function where you can input your personal information.
#The while loop is in case the user doesn't put an actual number. They will have to repeat their input.
def userPersonalInfo(): 
    yourName = input("Please enter your name: ")
    while True:
        try:
            yourAge = int(input("Please enter your age: "))
            break
        except:
             print("Please enter an actual number")
        
    yourAddress = input("Please enter your address: ")

    return yourName, yourAge, yourAddress

#The function which will display your gathered information in a sentence manner.
def infoDisplay(userNamePara, userAgePara, userAddressPara):
    print(f"Hi, my name is {userNamePara} and I am {userAgePara} years old. I live in {userAddressPara}.")

#The calling of the defined functions.
userName, userAge, userAddress = userPersonalInfo()
infoDisplay(userName, userAge, userAddress)

#A survey for room of improvements.
#Reminder that when this code is ran from Python terminal (the one with separate command line tab), when the input is invalid in the rating(int), the IDE will pop up to point out the error.
#When that happens, kindly go back to the Python command line interface and you will see the code still running.
#Although it won't be encountered in VS Code since I am running this from Visual Studio 2019 that runs code from a separate Python tab
while True:
    try:
        rating = int(input("How was our survey? Can you rate it from 1 - 5? 1 being the worst and 5 being the best: "))
        if rating == 1:
            print("Sorry it was horrible")
    
        elif rating == 2:
            print("Sorry it was mediocre")
   
        elif rating == 3:
            print("We will do our best to improve our survey")
    
        elif rating == 4:
            print("Thank you for your support!")
   
        elif rating == 5:
            print("Woah! Thank you for such an amazing rate, we will do our best to make more surveys!")

        else:
            error

        break
    except: 
        print("Please enter only numbers from 1 - 5")



    
         