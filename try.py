# mobile money
# welcome message
def greeting():
    greeting = input("welcome to mobile money")
    print(greeting)
greeting()
# menu options

def options():
    print("please select an option")
    print("1. Send Money") 
    print("2. Buy Airtime") 
    print("3. Check Balance")
options()



# this is the send money menu
def send_money():
    number = int(input("Please enter phone number: "))
    print(number)
    amount = int(input("Please enter amount: "))
    if amount > 50000:
        print("Insufficient funds")
    else:
        print( f"You have sent {amount} to {number}")


# Buy airtime
def buy_airtime():
    airtime = int(input("Please enter amount of airtime: "))
    if airtime < 500:
        print("Minimum airtime is 500")
    else:
        print("Airtime purchase successful")
 

# Check Balance    
def check_balance():
    if user_input == 3:
        print("Your balance is 50,000 UGX")

# this is the end session and it links back to the main menu
def endsession():
    user_input = int(input("Please enter 0 to go back to main and any other number to end: "))
    if user_input == 0:
        options()
    else:
        print("Successful Transaction")    
        
user_input =int(input("Please enter your choice: "))
if user_input == 1:
    send_money()
    endsession()

elif user_input == 2:
    buy_airtime() 
    endsession()

elif user_input == 3:
    check_balance()    
    endsession()
else:
    print("Invalid option selected")
    endsession()
endsession()


    