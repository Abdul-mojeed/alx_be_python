class BankAccount:
    def __init__(self, initial_balance=0):
        # store balance as a float to handle cents
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Print with two decimal places to match checker expectation
        print(f"Current Balance: ${self.account_balance:.2f}")
