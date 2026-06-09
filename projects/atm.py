# Working of ATM:
# Withdraw money
# Check balance
# mini statement
# pin change
# using dictionary for representing the data of users
accounts = {
    "678987632343": {"name": "Alex", "balance": 5000, "pin": 1234,},
    "987654321012": {"name": "Bob", "balance": 3000, "pin": 5678,},
    "123456789012": {"name": "Charlie", "balance": 7000, "pin": 9012,},
    "456789012345": {"name": "David", "balance": 10000, "pin": 3456,},
    "789012345678": {"name": "Eve", "balance": 2000, "pin": 7890,},
    "234567890123": {"name": "Frank", "balance": 8000, "pin": 2345,},
}
print("-"*60)
print("                           WELCOME               ")
print("-"*60)
acc_no = input("Enter your account number: ")
if acc_no in accounts:
    print("Proceed.")
    authorised = False
    for i in range(3):
        pin = int(input("Enter your pin: "))
        if pin == accounts[acc_no]["pin"]:
            print("Access granted.")
            authorised = True
            break
        elif i < 2:
            print(f"Incorrect pin. {2-i} attempts left.")
        else:
            print("Access denied.")
    
    if authorised:
        while True:
            print("These are the options: ")
            print("1. Withdraw money")
            print("2. Check balance")
            print("3. Mini statement")
            print("4. Pin change")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= accounts[acc_no]["balance"]:
                    accounts[acc_no]["balance"] -= amount
                    print(f"Please collect your cash. Your new balance is {accounts[acc_no]['balance']}.")
                else:
                    print("Insufficient balance.")
                input("Press Enter to continue...")

            elif choice == 2:
                print(f"Your current balance is {accounts[acc_no]['balance']}.")
                input("Press Enter to continue...")

            elif choice == 3:
                print("\n" + "="*60)
                print("                    MINI STATEMENT                     ")
                print("="*60)
                print(f"Account Number: {acc_no}")
                print(f"Name: {accounts[acc_no]['name']}")
                print(f"Balance: {accounts[acc_no]['balance']}")
                print("="*60 + "\n")
                input("Press Enter to continue...")

            elif choice == 4:
                old_pin = int(input("Enter your old pin: "))
                if old_pin == accounts[acc_no]["pin"]:
                    new_pin = int(input("Enter your new pin: "))
                    accounts[acc_no]["pin"] = new_pin
                    print("Pin changed successfully.")
                else:
                    print("Incorrect old pin.")
                input("Press Enter to continue...")

            elif choice == 5:
                print("Thank you for using our ATM.")
                break

            else:
                print("Invalid choice. Please try again.")
else:
    print("Invalid account number.")

#https://codeshare.io/5Xdz8l
accounts = {'62433570421': {'Name':'Alex',
                            'Balance': 3000,
                            'Pin': 1234},
            '62433570422': {'Name':'Bob',
                            'Balance': 10000,
                            'Pin': 5678},
            '62433570423': {'Name':'Charles',
                            'Balance': 50000,
                            'Pin': 1200},
            '62433570424': {'Name':'David',
                            'Balance': 30000,
                            'Pin': 9080},            
    }
print('-'*20)
print('    WELCOME    ')
print('-'*20)

user_acc = input('Please enter your account number: ')

if user_acc in accounts:
    crct_pin = accounts[user_acc]['Pin']
    c = 1
    authorised = True
    while c <= 3:
        user_pin = int(input('Please enter your Pin: '))
        if user_pin != crct_pin:
            remaining_attempts = 3-c
            if remaining_attempts == 0:
                authorised = False
                print('Account locked. Visit again')
            else:
                print(f'You have {remaining_attempts} attempts left')
        else:
            print('Proceed')
            break
        c+= 1
    transactions = []
    while authorised:
        print('These are the options')
        print('1.Withdrawl\n2.Deposit\n3.Balance Enquiry\n4.Ministatemet')
        print('5.Pin Change\n6.Exit')
        ch = int(input('Enter your choice no: '))
        if ch == 1:
            amount = int(input('Please enter the amount for withdrawl: '))
            if amount <= accounts[user_acc]['Balance']:
                print(f'Rs.{amount} withdrawn successfully')
                transactions.append(f'Rs.{amount} withdrawn')
                accounts[user_acc]["Balance"] -= amount
                print(f'Current balance: {accounts[user_acc]["Balance"]}')
            else:
                print('Insufficient balance')
            
        elif ch ==2:
            amount = int(input('Please enter the amount for deposit: '))
            accounts[user_acc]["Balance"] += amount
            print(f'Rs.{amount} deposited')
            transactions.append(f'Rs.{amount} deposited')
            print(f'Current balance: {accounts[user_acc]["Balance"]}')
        elif ch == 3:
            print(f'Current balance: {accounts[user_acc]["Balance"]}')
        elif ch == 4:
            n = len(transactions)
            if n <= 3:
                for i in transactions:
                    print(i)
            else:
                for i in range(n-3, n):
                    print(transactions[i])
        elif ch == 5:
            cur_pin = int(input('Please enter your current Pin: '))
            if accounts[user_acc]['Pin'] == cur_pin:
                new_pin = int(input('Please enter the new pin: '))
                confirm = int(input('Please confirm the new pin: '))
                if new_pin == confirm:
                    accounts[user_acc]['Pin'] = new_pin
                else:
                    print('Pin Confirmation failed')

            else:
                print('Entered wrong pin')
                          
        elif ch == 6:
            print('Thank you')
            break

        else:
            print('Invalid choice')

    
else:
    print('Invalid User')
