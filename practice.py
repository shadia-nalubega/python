def mobile_money():
    greeting = "welcome to mobile money"
    print(greeting)
mobile_money() 
# declaring another function for options on the menu
# these will be shown on the display panel
def option():
    print("1 Send Money")
    print("2 Buy Airtime")
    print("3 Check Balance")
option()

# we are creating the send money procedures. these will only be called in the options 
def send_money():
    number = int(input("Plese enter number: "))
    print(number)
    amount = int(input("Please enter amount: "))
    if amount >= 50000:
        print("insufficient funds")
    else:
        print("You have sent",amount,"to",number)
        # we do not call the function from here.
# we are now going to define another function called buy airtime
def buy_airtime():
    airtime = int(input("Please enter amount: "))
   
    if airtime > 500:
        print("Minimum airtime is 500")
    else:
        print("Airtime purchase successful")

# we are defining another function check balance
def balance():
    print("Your balance is 50,000 UGX")
# the continue option after transacting
def endsession():
    user_input= int(input("enter 0 to go to main other numbers to exit: "))
    if user_input == 0:
      option()
    else:
        print("Thank you for transacting with us")


def user_input():
# at this stage we are prompting the user to input their choice
    user = int(input("Please enter your choice: "))
    

    if user == 1:
        # at this moment we will call the mobile money function.but it can't be down, so we will create it up
        print("You have selected send money")
        send_money()
        endsession()
    elif user == 2:
        print("You have selected buy airtime")
        buy_airtime()
        endsession()
    elif user == 3:
        balance()
        endsession()
    else:
        print("invalid option")
        endsession()
user_input()
# at this point we want to avail the user with an option that can take them back to the main menu after transacting
# we will create it at the top and call it at every end of a transaction


