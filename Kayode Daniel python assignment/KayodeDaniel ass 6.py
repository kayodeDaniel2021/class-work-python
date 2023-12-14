# To Create a Simple Bank Account Management System

customerNames = ["Adewunmi Owolabi", "Adenike Ogunnaike"]
customerBalances = [70000, 90000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 2
i = 0

# Function to perform bank account operations
while True:
    # os.system("cls")
    print("Welcome to Zenith Bank Limited")
    print(" 1. Open a New Account ")
    print(" 2. Withdraw Funds ")
    print(" 3. Deposit Funds ")
    print(" 4. Check Customers & Balance ")
    print(" 5. Exit")

    choiceNumber = input("Kindly choose Your Option : ")
    if choiceNumber == "1":
        print("Option 1 is choosen by the Customer")
# The line below will take the no:of customers from the user.
        NOC = eval(input("Number of Customers : "))
 
        i = i + NOC
        if i > 2:
            print("\n")
            print("Customer Registration exceeded")
            i = i - NOC
        else:
            while counter_1 <= i:
# These few lines will append them to the list.
                name = input("Input Fullname : ")
                customerNames.append(name)
                deposition = eval(input("Enter Amount for Deposit to Open an Account : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print(customerBalances[counter_2], end="£")
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\nYour Account is Opened")
                print("Your Opening Balance is Deposited")
                print("Your Account Creation is Successful !")
                print("\n")
        mainMenu = input("Press Enter or Any Key to return to MAIN MENU...")
    elif choiceNumber == "2":
        j = 0
        print("Choice Option 2 is choosen by the Customer")
# This while loop will prevent the user using the account if the username is wrong.
        while j < 1:
            k = -1
            name = input("Pls, Enter Account Name : ")
# This while loop will keep the function running when variable k is smaller than length of the customerNames list.
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                        j = j + 1
                        print("Your Current Balance:", end="£")
                        print(customerBalances[k], end=" ")
                        print("\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Enter Value For Withdrawal : "))
                        if withdrawal > balance:
                            deposition = eval(input("Kindly make a deposit. Insufficient balance : "))
                            balance = balance + deposition
                            print("Your Current Balance:", end="£")
                            print(balance, end=" ")
                            print("\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("Withdrawal Successfull!")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end="£")
                            print("\n\n")
                        else:
                            balance = balance - withdrawal
# These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("Withdrawal Successfull!")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end="£")
                            print("\n\n")
            if j < 1:
# The if condition above would work when the name is wrong.
                print("Your Name does not match!\n")
                break
# This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Press Enter or Any Key to return to MAIN MENU....")
    elif choiceNumber == "3":
        print("Choice Number 3 is Selected by the Customer")
        n = 0
# The while loop below would work when the username is wrong.
        while n < 1:
            k = -1
            name = input("Please Enter Account Name : ")
            while k < len(customerNames) - 1:
                k = k + 1
# The two if conditions below would find whether the name is correct.
                if name == customerNames[k]:
                        n = n + 1
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        balance = (customerBalances[k])
# This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter Value Deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("Deposition successful!")
                        print("Your New Balance: ", balance, end="£")
                        print("\n\n")
            if n < 1:
                print("Your name does not match!\n")
                break
# This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Press Enter or Any Key to return to MAIN MENU...")
    elif choiceNumber == "4":
        print("Choice Number 4 is Selected by the Customer")
        k = 0
        print("Customers' Name and Balances below : ")
        print("\n")
# The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end="£")
            
            print("\n")
            k = k + 1
        mainMenu = input("Press Enter or Any Key to return to MAIN MENU...")
    elif choiceNumber == "5":
        
        print("Thank you for Banking with us!")
        print("\n")
        print("Goodbye!")
        break
    else:
        
        print("Invalid Option Selected by the Customer")
        print("Please Try again!")
        
        mainMenu = input("Press Enter or Any Key to return to MAIN MENU...")
 