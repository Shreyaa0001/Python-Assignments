class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number   
        self.balance = balance                 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

acc_no = input("Enter Account number:")
initial_balance = float(input("Enter account Balance"))
account = BankAccount( acc_no,initial_balance)

while True:
    print("\n.1.Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice ==1:
        amount = float(input("Enter amount to deposit:"))
        account.deposit(amount)
    elif  choice == 2 :
        amount = float(input("Enter amount to withdraw:"))
        account.withdraw(amount)
    elif choice == 3:
        account.check_balance()
        
    elif choice == 4:
        print("Thank you for using the bank system.")
        
    else:
        print("Invalid choice. Please try again.")            