#                                      ATM

#  Startmenu (Options will be displayed here)

def startmenu():
    print("Please select an option")
    print("Press 1 to deposit money")
    print("Press 2 to withdraw money")
    print("Press 3 to cancel the transaction")
    Input()
    
#  Descisions (Allow the users to choose an option)

def Input():
    Descision=input()
    Descision=int(Descision)
    if Descision>3:
        print("Invalid input")
        startmenu()
    else:
        if Descision==1:
            deposit_money()

        elif Descision==2:
            withdraw_money()
    
        elif Descision==3:
            End_session()
  
    
#  Deposit Menu

def deposit_money():
    dep_mon=int(input("Enter the amount to be deposited: "))
    if dep_mon < 0:
        print("Invalid Input")
        startmenu()
    else:
         New_bank_balance=dep_mon+bank_balance
         print("Your new bank balance is: {}".format(New_bank_balance))
         print("Thank you, have a nice day!")
         startmenu()
         
#  Withdraw Menu

def withdraw_money():
    with_mon=int(input("Enter the amount to be withdrawn: "))
    if with_mon < 0:
        print("Invalid Input")
        startmenu()
    else:
        New_bank_b=bank_balance-with_mon
    if New_bank_b < 0:
        print("Transaction not possible")
        startmenu()
    else:
        print("Your new bank balance is: {}" .format(New_bank_b))
        print("Thank you, have a nice day!")
        startmenu()
              
#  End Program

def End_session():
    print("This session has ended")
    print("Thank you, have a nice day!")
    print("Press ENTER to exit the program")
    input()

#  The program will take you towards Main Menu

def Welcome():
    if bank_balance < 0:
        print("Invalid Input")
        Welcome()
    else:
        print("Initiating....")
        startmenu()
        
#  The program starts from here:

print("Welcome To Bank")
bank_balance=int(input("Your Bank Balance: "))

Welcome()


