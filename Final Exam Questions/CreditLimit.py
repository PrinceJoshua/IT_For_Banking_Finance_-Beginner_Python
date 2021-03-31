creditLimit = 0
beginBalance = 0
totalPurchases = 0
MembershipType = 0
totalbalance = 0

def Member(MemberType, balance):
    if MemberType == "Bronze" and balance > 1500:
        return "Club credit  limit  exceeded"
    elif MemberType == "Silver" and balance > 3000:
        return "Club credit  limit  exceeded"
    elif MemberType == "Gold" and balance > 5000:
        return "Club credit  limit  exceeded"



def balCalc(beginBal,totalPurch, totalCred):
    newBalance = (beginBal + totalPurch) - totalCred
    return newBalance

def process():
    option = 1
    while option == 1:
        accountNumber = raw_input("What is the user Account Number ?\n")
        beginBalance = raw_input("Beginning Balance?\n")
        totalPurchases = raw_input("Total purchases? \n")
        totalCredit = raw_input("Total Credit Purchases?\n")
        MembershipType = raw_input("Membership Type? \n")

        beginBal = int(beginBalance)
        totalPurch = int(totalPurchases)
        totalCred = int(totalCredit)


        totalbalance = balCalc(beginBal,totalPurch,totalCred)
        membership = Member(MembershipType, totalbalance)

        option = raw_input("Do you want to continue ? \t 1- Yes 0- No\n")

        if option == "1":
            print "The Account number is ", accountNumber
            print "Membership Type : ", MembershipType
            print "The total Balance is: ", totalbalance
            if membership == None:
                print " "
            else:
                print membership

            print "\n"
            process()
        else:
            print "The Account number is ", accountNumber
            print "Membership Type : ", MembershipType
            print "The total Balance is: ", totalbalance
            if membership is None:
                print " "
            else:
                print membership
            exit()

process()





