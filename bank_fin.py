import random
accounts={}
def New_account():
    name=input("What is your name -")
    initial_deposit=float(input("your initial deposit="))
    account_number= random.randint(1000, 9999)
    accounts[account_number] = {
        'name': name,
        'balance': initial_deposit
    }
    print(account_number)
def deposit_funds():
    account_number=int(input("your account number"))
    if account_number in accounts:
        deposit_add=float(input("how much do you want to add ="))
        accounts[account_number]['balance']+=deposit_add
        print(f"your balance is={accounts[account_number]['balance']}")
    else:
        print("please try again, your account can not find")
def Withdraw_funds():
    account_number=int(input("your account number"))
    if account_number in accounts:
        Withdraw=float(input("how much do you want to Withdraw amount"))
        if Withdraw<accounts[account_number]['balance']:
            accounts[account_number]['balance']-=Withdraw
            print(f"your balance after it={accounts[account_number]['balance']}")
        else:
            print("Insufficient funds ser")
    else:
        print("wrong account number")
def check_balance():
    account_number=input("your account number>")
    if account_number in accounts:
        print(f"your balance={accounts[account_number]['balance']}")
    else:
        print("wrong account number")

def main():
    while True:
        print("1. Create a new account")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            New_account()
        elif choice == '2':
            deposit_funds()
        elif choice == '3':
            Withdraw_funds()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
