from datetime import datetime
date = datetime.now()
hours = date.hour
day = date.strftime("%m-%b-%Y")
account_balance = 5375.27


def Welcome():
    if hours < 12:
        print "Good Morning, Welcome to Sky Bank"
    elif hours >= 12 and  hours < 16:
        print "Good Afternoon, Welcome to Sky Bank"
    elif hours >= 16 and hours < 19:
        print "Good Evening, Welcome to Sky Bank"
    else:
        print "Good Night, Welcome to Sky Bank"

def GoodBye(account_balance):
    slip = raw_input(" Would you like to a Reciept ? Yes Or No ")
    print "\n"

    if slip == "Yes" or slip == "YES" or slip == "yes":

        if hours < 12:
            print "Good Morning, Thanks for Using Sky Bank"
            print "Date:  ", day
            print "ATM ID: WGM1K"
            print "Business Date: " , day
            print "Card Number:", "xxxxxx-xxxxx52"
            print "Account Balance: $%.2f" % account_balance, "\n"

        elif hours >= 12 and hours < 16:
            print "Good Afternoon, Thanks for Using Sky Bank"
            print "Date: ", day
            print "ATM ID: WGM1K"
            print "Business Date: ", day
            print "Card Number:", "xxxxxx-xxxxx52"
            print "Account Balance: $%.2f" % account_balance, "\n"
        elif hours >= 16 and hours < 19:
            print "Good Evening, Thanks for using Sky Bank"
            print "Date: ", day
            print "ATM ID: WGM1K"
            print "Business Date: ", day
            print "Card Number", "xxxxxx-xxxxx52"
            print "Account Balance: $%.2f" % account_balance, "\n"
        else:
            print "Good Night, Thanks Sky Bank"
            print "Date:  " , day
            print "ATM ID: WGM1K"
            print "Business Date: ",day
            print "Card Number:", "xxxxxx-xxxxx52"
            print "Account Balance: $%.2f"  % account_balance, "\n"
    else:
        if hours < 12:
            print "Good Morning, Thanks for Using Sky Bank"
        elif hours >= 12 and hours < 16:
            print "Good Afternoon, Thanks for Using Sky Bank"
        elif hours >= 16 and hours < 19:
            print "Good Evening, Thanks for using Sky Bank"
        else:
            print "Good Night, Thanks for using Sky Bank"


def atm_login():
    Welcome()
    pin_number = raw_input("Please Enter 4 digit Pin: ")
    while pin_number.__len__() != 4 or pin_number.__len__() > 4:
        pin_number = raw_input("Please Enter 4 digit Pin: ")
    print "\n"

    Process(account_balance)

def Balance(account_balance):
    print "Your current Balance : $%.2f" % account_balance, "\n"
    Process(account_balance)
    return account_balance



def Deposit(account_balance):
    dep_bal = raw_input(" How much do you want to Deposit ? \n")
    dep = float(dep_bal)
    if dep <= 0:
        print "Error cant deposit $0"
        try_again = raw_input(" Do you want to try again , Yes Or No")
        if try_again == "Yes" or try_again == " YES" or try_again == "yes":
            Deposit(account_balance)
        else:
            Process(account_balance)

    print "\n"
    print "Your current Balance : $%.2f" % account_balance
    print "Deposit: $%.2f" % dep

    account_balance = account_balance + dep
    print "New Balance: $%.2f"  % account_balance, "\n"
    Process(account_balance)
    return account_balance


def Withdrawl(account_balance):
    if account_balance == 0.0:
        print "Insufficient Funds $%2.f " % account_balance
        exit()
    with_drawl = raw_input("How much do you want to withdrawl ? \n")
    WD = float(with_drawl)

    if WD > account_balance:
        print "Insufficient Funds, Cannot withdrawl $%2.f " % WD
        Process(account_balance)
        print "\n"
    else:
        print "Your current Balance : $%.2f" % account_balance
        print "Withdrawl: $%.2f" % WD
        account_balance = account_balance - WD
        print "New Balance: $%.2f" % account_balance, "\n"
        Process(account_balance)
    return account_balance




def Process(account_balance):

    options = raw_input("Enter 1 - Balance \nEnter 2 - Deposit \nEnter 3 - Withdawl\nEnter 0 - Exit \n")

    option = int(options)

    while option != 0:
        if option > 4 :
            print "Please follow the instructions"
            Process(account_balance)
        if option == 1:
           Balance(account_balance)

        elif option == 2:
            Deposit(account_balance)

            Process(account_balance)

        elif option == 3:
            Withdrawl(account_balance)
        break
    else:
        GoodBye(account_balance)
        exit()
atm_login()