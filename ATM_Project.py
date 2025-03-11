
#create a Simple project using loop
'''
Q.1)ATM project in python that uses loop concepts to perform basic banking operations like:
1.checking balance
2.Depositing Money
3.Withdrawing Money
4.Exiting

e.g
deposite - amount----------3000
          5000+3000-------8000 ----------Check Balance

withdraw - amount----------2000
           8000-2000------6000 ----------check balance
'''
#solution
balance=5000

while True:
    print("ATM Machine")
    print("1.check balance")
    print("2.Deposite Money")
    print("3.Withdraw Money")

    number=int(input("enter your choice (1-4): "))

    if number==1:
        print(f"Your balance is:{balance}")
        input("Please enter to continue....")
    elif number==2:
        amount=int(input("Deposite the Amount: "))
        if amount>0:
            balance=balance+amount
            print(f"Rs.{amount} credited to your account. Total balance is :{balance}")
        
        else:
            print("Invalid credential please enter the correct amount")    
    elif number==3:
        amount1=int(input("enter the amount you want to withdraw:"))
        if 0 <amount1<balance:
            balance=balance-amount1
            print(f"Rs.{amount1} is withdrawn, Total Balance is{balance}")
        else:
            print("Invalid credential please enter the correct amount")      
    elif choice == 4:
        print("Exiting... Thank you for using our ATM.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")


        


